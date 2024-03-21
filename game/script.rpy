image bg office_background = "office.png"
image nik normal = "nik_normal.png"
image nik shy = "nik_shy.png"
image gala = "gala.png"
image luda angry = "luda_angry.png"
image luda shy = "luda_shy.png"
image luda = "luda.png"

define narrator = Character(None, color="#ffffff")
define nik = Character('Nikita', color="#c8ffc8")
define luda = Character('Ludmila Telegram', color="#d37f31")
define galla = Character('Galina', color="#1370ad")

label start:
    scene black
    narrator "Дело было в офисе одной государственной IT-конторы..."
    narrator "Ее название НИИ ТЗИ, там умные разработчики создают приложения, пишут код."
    narrator "На самом деле они просто сидят на своих рабочих местах и изображают бурную деятельность..."
    narrator "Автор данной новеллы - разработчик в этой компании... Был очередной день, когда я делал вид, что работаю..."
    narrator "Я начал писать код данной игры... Все равно никто не понимает что я там тыкаю..."
    scene bg office_background:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    with fade
    pause 0.5
    "Так выглядит наш офис. Дефолтная клетка для среднестатистического человека."
    "О! Смотри кто идет..."
    show nik normal
    with dissolve
    nik "Привет! Пошли за кофе и на курилку."
    show nik normal at right:
        xpos 0.8
    with dissolve
    pause 0.5
    show luda at left:
        xpos 0.8
    with dissolve
    luda "Куда-то собираетесь?"
    show nik shy at right:
        xpos 0.8
    with dissolve
    nik "Нет, мы тебя как раз и ждали..."
    show luda shy at left:
        xpos 0.8
    with dissolve
    luda "Правда?..."
    show nik normal at right:
        xpos 0.8
    pause 0.5
    show gala at left:
        xpos 0.3
    with dissolve
    galla "Не правда! Этот уебан обещал мне секс в клодовке... Я как раз захватила страпончик..."
    show nik shy at right:
        xpos 0.8
    nik "Точно! Как я мог забыть..."
    show luda angry at left:
        xpos 0.8
    with dissolve

    
    