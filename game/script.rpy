image bg office_background = "office.png"
image nik normal = "nik_normal.png"

define nik = Character('Nikita', color="#c8ffc8")

label start:
    scene black
    "Дело было в офисе одной государственной IT-конторы..."
    scene bg office_background:
        zoom 1.0
    with fade
    show nik normal
    nik "I want to suck"
    #hide nik
    "Test end"