import datetime

widgets = {
}


def assign(i, j):
    global widgets

    def the_real_decorator(function):
        widgets[(i, j)] = function
        return function
    return the_real_decorator


@assign(0, 0)
def clock(request, coordinates, counter, time_lapse):
    if counter % 2 == 1 and time_lapse < 500:
        return

    now = datetime.datetime.now()
    t = "{t.hour:02d}:{t.minute:02d}:{t.second:02d}".format(t=now)
    return {
        'html': t
    }


@assign(0, 1)
def color(request, coordinates, counter, time_lapse):

    content = {}

    if counter == 0:
        content['html'] = """
            <div id="the-text" class="text-center">?</div>
        """
    else:
        content['elements'] = {
            '#the-text': counter,
        }

    if counter % 2 == 0:
        bgcolor = 'black'
        fgcolor = 'white'
    else:
        bgcolor = 'white'
        fgcolor = 'black'

    content['css'] = {
        'background-color': bgcolor,
        'color': fgcolor
    }

    return content
