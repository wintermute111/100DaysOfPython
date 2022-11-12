import pandas

from turtle import Turtle, Screen

FONT = ("Courier", 10, "normal")

scr = Screen()
scr.bgpic("blank_states_img.gif")
scr.title("US States Game")

states = pandas.read_csv("50_states.csv")
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.color("black")
turtle.speed(0)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = scr.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states.state.values:
            if state not in guessed_states:
                missing_states.append(state)
        output_df = pandas.DataFrame(missing_states)
        output_df.to_csv("states_to_learn.csv")
        break
    if answer_state in states.state.values:
        guessed_states.append(answer_state)
        answer_state_coordinates = (int(states[states.state == answer_state].x),
                                    int(states[states.state == answer_state].y))
        turtle.goto(answer_state_coordinates)
        turtle.write(answer_state, align="center", font=FONT)

