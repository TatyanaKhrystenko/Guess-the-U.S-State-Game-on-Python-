import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

file = pandas.read_csv("50_states.csv")
state_list = file.state.to_list()

quessed_states = []
while len(quessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(quessed_states)}/50 guessing states",
                                     prompt="What is the next state?").title()


    if answer_state == "Exit":
        missing_state = [state for state in state_list if state not in quessed_states]
        data = pandas.DataFrame(missing_state)
        data.to_csv("states_to_learn")
        break
    if answer_state in state_list:
        state_row = file[file.state == answer_state]
        state_x = int(state_row.x)
        state_y = int(state_row.y)

        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.setposition(x=state_x, y=state_y)
        state.write(answer_state)
        quessed_states.append(answer_state )
        state_list.remove(answer_state)



