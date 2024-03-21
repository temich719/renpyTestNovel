image bg office_background = "office.png"
image nik normal = "nik_normal.png"
image nik shy = "nik_shy.png"
image gala glitched = "gala.png"
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
        ypos 0.9
    with dissolve
    pause 0.5
    show luda at left:
        xpos 0.8
        ypos 0.9
    with dissolve
    luda "Куда-то собираетесь?"
    show nik shy at right:
        xpos 0.8
        ypos 0.9
    with dissolve
    nik "Нет, мы тебя как раз и ждали..."
    show luda shy at left:
        xpos 0.8
        ypos 0.9
    with dissolve
    luda "Правда?..."
    show nik normal at right:
        xpos 0.8
        ypos 0.9
    pause 0.5
    show gala at left:
        xpos 0.3
        ypos 0.9
    with dissolve
    galla "Не правда! Этот уебан обещал мне секс в клодовке... Я как раз захватила страпончик..."
    show nik shy at right:
        xpos 0.8
        ypos 0.9
    nik "Точно! Как я мог забыть..."
    show luda angry at left:
        xpos 0.8
        ypos 0.9
    with dissolve
    luda "{b}А как же я?...{/b}"
    narrator "Ему придется выбрать: быть под влиянием каблука Людмилы, либо пассивным сексуальным партнером Галины..."
    menu:
        "Каблук":
            "Вы выбрали, быть каблуком."
            call love()
        "Пассив":
            "Вы выбрали давать в попу..."
            call sex()

label love():
    scene bg office_background:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    with fade
    show nik normal at right:
        xpos 0.8
        ypos 0.9
    with dissolve
    show luda shy at left:
        xpos 0.8
        ypos 0.9
    with dissolve
    luda "Я так рада, что встретила тебя... Как раз хотела тебе подарить золотой дождик... Твой любимый... Ты меня не подвел."
    show nik shy at right:
        xpos 0.8
        ypos 0.9
    with dissolve
    pause 1.5
    scene bg gray
    with fade
    narrator "На такой положительной ноте повествование подходит к концу... Всем такой же крепкой любви как у Никиты и Люды!"
    pause 2.0

label sex():
    scene bg office_background:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    with fade
    show nik normal at right:
        xpos 0.8
        ypos 0.9
    with dissolve
    show gala at left:
        xpos 0.3
        ypos 0.9
    with dissolve
    nik "Прости Люда... Я еще молод и горяч, страпон так и манит..."
    galla "Иди ко мне мой малыш..."
    show nik shy at right:
        xpos 0.8
        ypos 0.9
    with dissolve
    pause 1.5
    scene black
    with fade
    narrator "Под жалкие стоны Никиты и удовлетворенные вопли Галины я завершу свое мини повествование о сегодняшнем дне..."
    narrator "Нет повести печальнее на свете, чем повесть #glitch о Никите и минете...#"
    pause 2.0
#Буквы
#Эфеект молнии
#Тряска
#звуки стонов, молнии, и тихая музыка с птицами



    
    