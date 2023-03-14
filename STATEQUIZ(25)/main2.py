import turtle
import pandas as pd

df = pd.read_csv("D:/안도윤/2. 3월/vscode/python100project/DAY25/50_states.csv")
df.info()

screen = turtle.Screen()
screen.title("U.S.A. states game")

screen.bgpic("D:/안도윤/2. 3월/vscode/python100project/DAY25/blank_states_img.gif")

states_lists = df["state"].to_list()

df.head()

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 states",
        prompt = "What's another state's name?").title()
    if answer_state in states_lists:
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        guessed_state.append(answer_state)
        matched_data = df[df["state"] == answer_state]
        t.goto(int(matched_data.x), int(matched_data.y))
        t.write(answer_state)
screen.exitonclick()
    