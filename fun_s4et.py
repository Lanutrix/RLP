from lol import *
from nepon import *
th = os.getcwd()+"/scr/img"
print(th)

text=""

def forFrame(frame_number, output_array, output_count):
    global text
    text=dep(frame_number,output_array,text)


isxod=[
            {'box_points': (362, 295, 443, 355), 'name': 'boat', 'percentage_probability': 26.666194200515747},
            {'box_points': (319, 245, 386, 296), 'name': 'boat', 'percentage_probability': 30.052968859672546},
            {'box_points': (219, 308, 341, 358), 'name': 'boat', 'percentage_probability': 47.46982455253601},
            {'box_points': (589, 198, 621, 241), 'name': 'bus', 'percentage_probability': 24.62330162525177},
            {'box_points': (519, 181, 583, 263), 'name': 'bus', 'percentage_probability': 27.446213364601135},
            {'box_points': (493, 197, 561, 272), 'name': 'bus', 'percentage_probability': 59.81815457344055},
            {'box_points': (432, 187, 491, 240), 'name': 'bus', 'percentage_probability': 64.42965269088745},
            {'box_points': (157, 225, 220, 255), 'name': 'car', 'percentage_probability': 21.150341629981995},
            {'box_points': (324, 249, 377, 293), 'name': 'car', 'percentage_probability': 24.089913070201874},
            {'box_points': (152, 275, 260, 327), 'name': 'car', 'percentage_probability': 30.341443419456482},
            {'box_points': (433, 198, 485, 244), 'name': 'car', 'percentage_probability': 37.205660343170166},
            {'box_points': (184, 226, 233, 260), 'name': 'car', 'percentage_probability': 38.52525353431702}, 
            {'box_points': (3, 296, 134, 359), 'name': 'car', 'percentage_probability': 47.80363142490387}, 
            {'box_points': (357, 302, 439, 359), 'name': 'car', 'percentage_probability': 47.94844686985016}, 
            {'box_points': (481, 266, 546, 314), 'name': 'car', 'percentage_probability': 65.8585786819458}, 
            {'box_points': (597, 269, 624, 318), 'name': 'person', 'percentage_probability': 27.125394344329834}
            ]
for i in range(100,109):
    forFrame(i,isxod,0)
nastr(text)