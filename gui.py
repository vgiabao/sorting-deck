from pyglet import resource, text, clock, app
from pyglet.window import Window, mouse
# from pyglet.gl import glEnable, glBlendFunc, GL_SRC_ALPHA, \
#                       GL_ONE_MINUS_SRC_ALPHA, GL_BLEND


window = Window(width=600, height=1000)
array = []
step = []
list_draw = []
cost = 0
number_up = 0
number_down = 0
distance = 0
count_out = 0
kindly = ''
part_of_steps = []
background = resource.image('kitten.jpg')
plane = resource.image('maybay.png')
arrow1 = resource.image('arrow.png')
arrow2 = resource.image('arrow.png')


'''
print label in screen, each number is represented by one label
'''


def number_label(array):
    global list_draw, step
    cost = 0
    for index in range(len(array)):
        cost += 66
        number_label = text.Label(str(array[index]), x=275,
                                  y=-(15-len(array))/2*66+1000 - cost,
                                  font_name='Arial', font_size=20)
        list_draw.append(number_label)


def label(texty, y):
    label = text.Label(texty, x=335, color=(255, 0, 0, 255), y=y,
                       font_name='Arial', font_size=20,)
    return label


'''

describe: function dung de thiet lap mau sac, nhap gia tri ban dau cho cac
bien global, mau sac ket thuc
dat mot bien cost = 0 de giao tiep giua drow and on key

'''


def buble_foundation():
    global list_draw, step, array, cost, number_up, number_down, distance, \
      detailed_list, part_of_steps, count_out
    if cost == 0:
        if detailed_step:
            part_of_steps = detailed_step.pop(0)
            for item in list_draw:
                item.color = 255, 255, 255, 255
                down_point = list_draw[part_of_steps[1]]
                up_point = list_draw[part_of_steps[0]]
                down_point.color = 255, 0, 0, 255
                up_point.color = 255, 0, 0, 255
            if step and part_of_steps == step[0]:
                i, j = step.pop(0)
                number_up = i
                number_down = j
                distance = abs(i - j) * 66
                cost += 1
        else:
            count_out = 1
            for item in list_draw:
                item.color = 255, 0, 0, 255
    return


'''
describe: function nay de di chuyen cac label tren mang hinh window
'''


def buble_draw():
    global list_draw, number_up, number_down, cost
    label(str(array[number_up])+' > '+str(array[number_down]), 800).draw()
    list_draw[number_up].color = 255, 0, 0, 255
    list_draw[number_down].color = 255, 0, 0, 255
    list_draw[number_up].y = list_draw[number_up].y - 5
    list_draw[number_down].y = list_draw[number_down].y + 5
    arrow1.blit(175, list_draw[number_up].y - 30)
    arrow2.blit(175, list_draw[number_down].y - 30)
    cost += 5
    return


def insert_draw():
    global list_draw, number_up, number_down, cost
    list_draw[number_up].y = list_draw[number_up].y + 5
    for item in list_draw[number_down:number_up]:
        item.color = 0, 0, 255, 255
        item.y = item.y - 5/abs(number_up - number_down)
    cost += 5


'''
function nay dung de xu li label dua theo gia tri cua bien cost(global) va bien
kiem tra ket thuc di chuyen(count_out(global))
'''


def draw():
    global list_draw, step, array, cost, number_up, number_down, \
        distance, kind, detailed_step, part_of_steps, count_out
    if cost <= 2:
        if part_of_steps and count_out == 0:
            up = part_of_steps[1]
            down = part_of_steps[0]
            if up != down:
                label('Comparing ' + str(array[up]) + ' and ' +
                      str(array[down]), 800).draw()
            arrow1.blit(175, list_draw[up].y - 30)
            arrow2.blit(175, list_draw[down].y - 30)
        elif count_out == 1:
            label('The list is sorted', 750).draw()
    elif cost > 2 and cost < distance:
        if kind is 'bubble':
            buble_draw()
        elif kind is 'insert':
            insert_draw()
    elif cost >= distance:
        if kind is 'bubble':
            list_draw[number_up], list_draw[number_down] = \
                    list_draw[number_down], list_draw[number_up]
            array[number_up], array[number_down] = array[number_down], \
                array[number_up]
            cost = 0
            list_draw[number_up].color = 255, 0, 0, 255
            list_draw[number_down].color = 255, 0, 0, 255
        if kind is 'insert':
            for index in range(number_up, number_down, -1):
                list_draw[index], list_draw[index - 1] \
                    = list_draw[index - 1], list_draw[index]
                array[index], array[index - 1] = array[index - 1], array[index]
            list_draw[number_up].color = 255, 0, 0, 255
            cost = 0


'''
short description: function nay dung de thao tac giua window va chuot
'''


@window.event
def on_mouse_press(x, y, button, modifier):
    global list_draw, step, array, cost, number_up, number_down, distance
    if button == mouse.LEFT:
        buble_foundation()
        if cost == 1 or cost == 2:
            list_draw[number_up].color = 255, 0, 0, 255
            list_draw[number_down].color = 255, 0, 0, 255
            cost += 1


@window.event
def on_draw():
    window.clear()
    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    background.blit(0, 0)
    for number_label in list_draw:
        plane.blit(number_label.x - 25, number_label.y - 30)
        number_label.draw()
    draw()


def update(dt):
    return


clock.schedule_interval(update, 1/40)


'''
khoi tao gia tri ban dau cua bien, dua tren chuong trinh goc(sorting_deck),
chay pyglet
'''


def mainly(first, simple_moving_list, kindly, detailed_list):
    global list_draw, step, array, cost, number_up, number_down, kind, \
     detailed_step
    step = simple_moving_list
    array = list(first)
    kind = kindly
    detailed_step = detailed_list[:]
    number_label(array)
    app.run()
