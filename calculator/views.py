from django.shortcuts import render
import math
from calculator.models import Point
from django.contrib import messages


def index(request):
    return render(request, 'input.html')


def displayAll(request):
    points = Point.objects.all()
    return render(request, "display.html", {"points": points})


def saveBLH(request):
    longitude = request.GET['longitude']
    latitude = request.GET['latitude']
    name = request.GET['ID']

    Point(name=name, latitude=latitude, longitude=longitude).save()

    # messages.info(request, str(name) + ' was added to base!')
    return render(request, "input.html")


def saveXYZ(request):

    x = float(request.POST['x'])
    y = float(request.POST['y'])
    z = float(request.POST['z'])

    name = str(request.POST['ID'])

    Point(name=name, x=x, y=y, z=z).save()

    # messages.info(request, str(name) + ' was added to base!')
    return render(request, "input.html")


def toLatLong(request):

    x = request.POST['X']
    y = request.POST['Y']
    z = request.POST['Z']
    name = request.POST['ID1']

    if x.isdigit() and y.isdigit() and z.isdigit():
        # Большая полуось
        a = 6378245
        # Обратное сжатие
        F = 298.3
        x = float(x)
        y = float(y)
        z = float(z)
        f = 1 / F
        e2 = 2 * f - f ** 2
        p = math.sqrt(x ** 2 + y ** 2)
        r = math.sqrt(p ** 2 + z ** 2)
        m = math.atan((z / p) * ((1 - f) + ((a * e2) / r)))
        latitudetop = z * (1 - f) + e2 * a * math.sin(m) ** 3
        latitudebot = (1 - f) * (p - e2 * a * math.cos(m) ** 3)
        longitude = math.atan(y / x)
        latitude = math.atan(latitudetop / latitudebot)
        longitude = math.pi + longitude if longitude < 0 else longitude
        lon_deg = (longitude / math.pi) * 180
        lat_deg = (latitude / math.pi) * 180
        h = p * math.cos(latitude) + z * math.sin(latitude) - a * math.sqrt(1 - e2 * math.sin(latitude) ** 2)
        B = [round(lat_deg),
             round((lat_deg - round(lat_deg)) * 60),
             round(3600 * (lat_deg - round(lat_deg) - (round((lat_deg - round(lat_deg)) * 60) / 60)))]
        L = [round(lon_deg),
             round((lon_deg - round(lon_deg)) * 60),
             round(3600 * (lon_deg - round(lon_deg) - (round((lon_deg - round(lon_deg)) * 60) / 60)))]
        Point(name=name, latitude=latitude, longitude=longitude, x=x, y=y, z=z).save()
        return render(request, "resultBLH.html", {"BGrad": B[0], "BMin": B[1], "BSec": B[2],
                                                  "LGrad": L[0], "LMin": L[1], "LSec": L[2],
                                                  "H": h, 'latitude': latitude, 'longitude': longitude, 'ID': name})
    else:
        return render(request, "input.html")


def fromLatLong(request):
    BGrad = request.POST['BGrad']
    BMin = request.POST['BMin']
    BSec = request.POST['BSec']
    LGrad = request.POST['LGrad']
    LMin = request.POST['LMin']
    LSec = request.POST['LSec']
    H = request.POST['H']
    name = request.POST['ID2']
    if BGrad.isdigit() and BMin.isdigit() and BSec.isdigit() \
            and LGrad.isdigit() and LMin.isdigit() and LSec.isdigit() and H.isdigit():
        # Большая полуось
        a = 6378245
        # Обратное сжатие
        F = 298.3
        BGrad = int(BGrad)
        BMin = int(BMin)
        BSec = int(BSec)
        LGrad = int(LGrad)
        LMin = int(LMin)
        LSec = int(LSec)
        BDec = math.fabs(BGrad) + math.fabs(BMin / 60) + math.fabs(BSec / 3600)
        LDec = math.fabs(LGrad) + math.fabs(LMin / 60) + math.fabs(LSec / 3600)
        BDec = - BDec if BGrad < 0 or BMin < 0 or BSec < 0 else BDec
        LDec = - LDec if LGrad < 0 or LMin < 0 or LSec < 0 else LDec
        BRad = BDec / 180 * math.pi
        LRad = LDec / 180 * math.pi
        H = int(H)
        f = 1 / F
        e2 = 2 * f - f ** 2
        n = a / math.sqrt(1 - e2 * math.sin(BRad)**2)
        X = (n + H) * math.cos(BRad) * math.cos(LRad)
        Y = (n + H) * math.cos(BRad) * math.sin(LRad)
        Z = ((1 - e2) * n + H) * math.sin(BRad)
        latitude = BGrad * math.pi / 180
        longitude = LGrad * math.pi / 180
        Point(name=name, latitude=latitude, longitude=longitude, x=X, y=Y, z=Z).save()
        return render(request, "resultXYZ.html", {"X": X, "Y": Y, "Z": Z, "ID": name})
    else:
        return render(request, "input.html")
