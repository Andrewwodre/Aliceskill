real_story = '''Парень задолжал очень большую сумму местному банку. Он провел вечер в баре и сильно напился. 
Вернувшись домой, он забыл закрыть дверь. Пришедшие за ним коллекторы вломились в дом и начали ему угрожать, 
он выдал место хранения ценных вещей. Коллекторы забрали все драгоценности и ушли, а пьяный парень в бреду пришел к 
выводу, что жить смысла больше нет и повесился. '''


__evidences = [[
    'Тело было найдено матерью погибшего на следующий день после смерти, он был повешен на петле, под его ногами была опрокинутая табуретка.',
    'Соседи заявили, что парень возвращался домой поздно вечером очень пьяным.',
    'Мать утверждала, что ее сын был очень жизнерадостным человеком и никогда бы такого не совершил.',
    'Выяснилось, что у парня было множество долгов.',
    'При обыске квартиры обнаружили пропажу ценных вещей.'], ['На теле погибшей нет следов насилия, эксперты определили, что смерть произошла от отравления.',
             'При опросе слуг определили двух людей, возможно причастных к смерти женщины. Повар часто жаловался на маленькую зарплату и на то, как с ним обращаются хозяева. А про гувернантку давно ходит немало слухов о том, что она любовница хозяина дома.',
             'И повар и гувернантка отрицали свою вину и утверждали, что никак не могли быть причастны к смерти хозяйки.',
             'На кухне повара был найден мышьяк']]

stor = [['''"Здравствуйте детектив! Вы как раз вовремя, давайте я вас провожу к погибшему", - голос полицейского казался неестественно звонким. "Спасибо, я разберусь", - не убирая прилипшую к губам сигарету, ответил Джейкоб. Блэк поднялся по лестнице и увидел дверь с характерной желто-черной лентой. Он приложил немало усилий, пытаясь открыть ее, но все было напрасно - дверь не поддавалась. Помогите Джейкобу открыть дверь - ответьте на загадку.''',
'''Из соседней двери вышел мужчина в темном фраке и закурил, бросив жалобный, но в то же время осудительный взгляд на дверь в квартиру погибшего. Когда сосед уже почти ушел, Джейкоб крикнул ему вслед: "Постойте, мистер". Блэк подошел к мужчине и хотел было расспросить его о том, что ему известно о погибшем, но заметил, что мужчина сильно нервничает и торопится побыстрее уйти. Сосед явно что-то знает, помогите Блэку разговорить незнакомца - разгадайте загадку.''',
 '''Блэк вышел из мрачного подъезда и уже собирался уходить. "Постойте, постойте!" - плачущим голосом закрчиала женщина вслед детективу. Обернувшись, Джейкоб увидел, как странная женщина подбежала к полицейской машине, преграждавшей путь к подъезду. Женщина кричала, но полицейские не пускали ее. Блэк подошел к патрульному и попросил его пропустить эту женщину. Полицейский нахмурился и с недоверием посмотрел на детектива. Помогите Блеку получить расположение полицейского - ответьте на загадку.''',
 '''В кошельке Ричарда Блэк нашел визитку печально известного банка "Сент-Льюис". Блэк сразу же отправился туда. "Я хочу узнать подробности о счете Ричарда Паркера. Вот мое удостоверение", - Блэк обратился к администратору банка. "Извините, эта информация конфиденциальна", - коротко ответил администратор и ушел в свой офис. Немного осмотревшись, Блэк замечает открытую дверь в архив... Разгадайте загадку и Джейкоб останется незамеченным.''',
 '''Уже придя домой, Джейкоб услышал гудок телефона. Он сильно устал за сегодня и надеялся хорошо отдохнуть, но, увидев на экране мобильного звонок от начальства, он понял, что отдохнуть сейчас точно не получится. "Внимание... Джейкоб... Мы получили очень важную... Это многое..." - звук был настолько ужасным, что Блэк едва мог разобрать отдельные слова. "Нужно срочно починить антенну!" - Джейкоб вспомнил о сломанной антенне, которую он забывал починить уже несколько дней. Помогите детективу разобраться со сломанной антенной, ответьте на загадку'''],
['''Джейкоб зашел в поместье, в котором на днях умерла хозяйка, и окинул взглядом просторные залы и лестницы, ведущие на второй этаж. По пути к месту допроса он встретил экспертов, которые уже должны были сделать заключение о причине смерти. Они ожесточенно спорили о чем-то. Разрешите спор экспертов - ответьте на загадку.''',
'''Блэк прошел к лестнице, за которой шептались две обеспокоенные молодые служанки. Детектив решил прислушаться к их сплетням. Помогите Джейкобу утаиться – ответьте на загадку.''',
'''Блэк продолжил подниматься по длинной лестнице на второй этаж, где находилось место проведения допроса. Поднявшись, он огляделся. Второй этаж оказался настоящим лабиринтом из коридоров и комнат. Помогите Джейкобу найти нужную комнату – ответьте на загадку.''',
'''Джейкоб вернулся на первый этаж и уже собрался уходить, но что-то не давало ему покоя. Он обратил свой взгляд в сторону кухни, он чувствовал, что там что-то важное. Блэк не стал игнорировать это чувство и подошел к двери кухни. На ней висел крепкий металлический замок. Помогите Джейкобу найти ключ - ответьте на загадку.''', ],
 ['Джейкоб медленно поднялся по старой скрипучей лестнице и остановился перед дверью квартиры, где на днях был убит старик. За соседней дверью послышался громкий шорох, кого-то явно интересовал детектив. Помогите Блэку вывести соседей на разговор – ответьте на загадку.',
 'Блэк дернул за ручку двери – она оказалась не заперта. Войдя внутрь, он осмотрелся: интерьер был скудный, в воздухе летала пыль, а обои были пожелтевшими и ободранными. В углу он заметил крепко спящую в кресле старуху. Помогите Блэку ее разбудить – ответьте на загадку.',
  'Блэк продолжил расследование. Слева от старухи находилась дверь. Дёрнув за ручку, детектив ее открыть не смог. Она закрыта на ключ, и, скорее всего, за ней находится тело жертвы. Помогите Блэку найти ключ – ответьте на загадку.',
  'Вздохнув, Джейкоб направился на кухню. Там он встретил женщину с мужчиной, они сидели за грязным столом и старались не обращать внимания на детектива. На его приветствие и вопросы никто не отвечал. Помогите Блэку разговорить их – ответьте на загадку.']]


sucv = [[
 'Наконец, приложив нечеловеческие усилия, Джейкоб смог отворить эту дверь, немного изучив комнату и тело погибшего он записал первую улику к себе в дневник:',
 '''"Милейший, не думайте ничего плохого, я не из полиции, - Блэк старательно успокаивал мужчину в темном фраке, - мне лишь крайне любопытно узнать: быть может, вы знаете что-то о вашем погибшем соседе?" "Черт с тобой!" - ответил мужчина и начал свой рассказ о вчерашнем вечере... Так в дневнике Блэка появилась новая улика: ''',
'''Сильно нехотя полицейский согласился пропустить даму. "Вы умеете убеждать, Джейкоб", - с сильным недовольством он обратился к детективу. "Спасибо, товарищ, я у вас в долгу", - ответил ему Блэк. Джейкоб провел женщину к ближайшей лавочке, успокоил, рассказал, что он детектив, которому поручено расследовать это дело и внимательно выслушал все, что она ему рассказала. Так у Блэка появилась новая запись в дневнике: ''',
'''Пробравшись сквозь толпу клерков, Блэк ловко заныривает в архив. Перерыв с полсотни различных документов, он наконец нашел нужные ему. Не тратя время на радость, он смог сбежать из помещения за секунду до прихода работника. Так в дневнике детектива появилась новая запись: ''',
'''"Давай же! Ну давай... Да! Работает!" - Джейкоб все же смог починить злополучную антенну. То, что он услышал от своих коллег, сильно шокировало Блэка... "Это и правда многое меняет..." - все, что смог вымолвить детектив перед тем как помчаться в отдел. Вот, что он узнал: '''],
  ['''Джейкобу удалось разрешить спор экспертов и в дневнике Блэка появилась новая запись: ''',
'''Девушки проболтали недолго и разошлись почти сразу, но прослушанной информации Джейкобу было достаточно, чтобы сделать новую запись в своем дневнике: ''',
'''Пройдя несколько коридоров, детектив нашел нужную дверь. Он зашел в комнату и начал опрашивать главных подозреваемых: повара и гувернантку. Вот, что записал Блэк к себе в дневник: ''',
'''Тщательно осмотрев место вокруг, Блэк нашел блестящий ключ под одной из ваз, стоящих рядом. Джейкоб вошел в кухню и обыскал каждый ее уголок. В одном из ящиков под грудой различных приборов для готовки нашлась небольшая баночка с мышьяком. Блэк записал эту улику к себе в дневник: '''],
['Джейкоб постучался в соседнюю дверь, она тут же отворилась, его встретили взволнованные соседи, которых неимоверно интересовало произошедшее. Они сразу же начали давать свои показания детективу, не дожидаясь вопроса. Так в дневнике Блэка появилась запись: ',
 'Немного пошатав старушку, Джейкоб смог ее разбудить. Она извинилась перед детективом, и он начал допрос. Старуха вела себя очень странно и оказалась слишком суеверной, но детективу важны любые материалы. Он записал себе в дневник следующее: ',
 'Пошарившись в карманах уснувшей старухи, он нашел небольшой ключик, который идеально подошел к двери. Детектив вошел внутрь, внимательно изучил труп и осмотрел всю комнату, стараясь не упустить ни одной детали. Так в его дневнике появилась новая запись: ',
 'Всё-таки опытному детективу удалось вывести женщину на разговор, а мужчина так ни слова и не произнес. Допрос продлился недолго, женщина говорила нехотя и очень тихо. Но предоставленной информации Джейкобу было достаточно, чтобы записать в дневник последнюю улику: ']]

loose = [[
 'Ржавая ручка так и не поддалась детективу, к сожалению, зацепки по этому делу ему придется искать в другом месте.',
 '"Мне некогда!" - рявкнул мужчина и скрылся прежде чем Джейкоб смог что-либо предпринять.',
 '''Грозно посмотрев на него и отвернувшись, полицейский дал понять Джейкобу, что не пропустит эту даму.,
Что же, придется Блэку искать улики в другом месте.''',
 '''Стоило Блэку войти в помещение архива, как его тут же поймали охранники, заметившие этот дерзкий
поступок детектива. Сильно церемониться с Блэком не стали, но, к счастью для него, банку хватало различных скандалов
и его просто выкинули из здания.''',
 '''"Да, электрик из меня явно хуже чем детектив", - заключил Джейкоб. 
"Не страшно, кажется я уже понял что к чему", - он второпях надел на себя фрак и направился в отдел. '''
], ['''Пока детектив думал, эксперты скрылись из виду. Придется искать другие улики.''', '''Девушки заметили грозную фигуру у лестницы и, испугавшись, быстро убежали в подсобку.''',
   '''Потратив приличное количество времени на поиск комнаты допроса, детектив так и не смог найти нужную ему дверь. 
День близится к вечеру, нужно искать другие улики.''', '''Блэк тщательно осмотрел все вокруг, но так и не смог найти ключ. Похоже, повар носит его с собой. 
Детектив тяжело вздохнул, развернулся и ушел, оставив мучащее его место.'''],
['Джейкоб постучался в соседнюю дверь, но никто не ответил. Суетливый шорох также затих. Придется искать улики собственно в самой квартире.',
 'Как бы Джейкоб ни старался разбудить старушку, она так и не проснулась. Похоже, она приняла какие-то таблетки и накрепко уснула. Придется искать материалы по делу в другом месте.',
 'Сыщик нашел несколько ключей, но, к сожалению, ни один из них не подошел. Придется искать улики в другом месте.',
 'Проговорив в одиночку несколько минут, Джейкоб так и не получил ответа. Ничего не поделаешь, на этом расследование заканчивается. Время возвращаться.']]