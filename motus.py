import streamlit as st
import random
import pandas as pd

wordList = pd.read_feather('test')['Words'].tolist()

# leMot = random.choice(wordList)

def gamemode():
    st.header("Game mode")

def solver():
    st.header("Solver mode")
    guess = st.text_input('Met ton mot la (mettre un 0 si on connait pas la lettre)').upper()
    print("onela")
    # 1ere selection, on garde que les mots de meme longuer
    listMotPossible = []
    for mot in wordList:
        if len(guess) == len(mot):
            listMotPossible.append(mot)
    # 2eme selection, on garde que les mots avec les lettres a la bonne place
    to_del = []
    for mot in listMotPossible:
        toDelete = False
        for i in range(len(guess)):
            if guess[i] != '0':
                if mot[i] != guess[i]:
                    toDelete = True
        if toDelete:
            to_del.append(mot)
    for mot in to_del:
        listMotPossible.remove(mot)

    letterInButNoIdeaWhere = st.text_input('Lettre qui est dans le mot mais on sait pas ou maggle').upper()
    # 3eme selection, on garde que les mots avec les lettres correpondantes mais pas a leurs place
    to_del = []
    if len(letterInButNoIdeaWhere) != 0:
        for i, v in enumerate(letterInButNoIdeaWhere):
            for mot in listMotPossible:
                if v not in mot:
                    to_del.append(mot)
        for mot in to_del:
            try:
                listMotPossible.remove(mot)
            except:
                pass

    # 4eme selection, on vire les mots comprennant les lettres interdites
    forbiddenLetters = st.text_input('Lettre qui SONT PAS dans le mot').upper()
    to_del = []
    if len(forbiddenLetters) != 0:
        for i, v in enumerate(forbiddenLetters):
            print(v)
            for mot in listMotPossible:
                if v in mot:
                    to_del.append(mot)
        for mot in to_del:
            try:
                listMotPossible.remove(mot)
            except:
                pass


    if len(listMotPossible) != 0:
        for mot in listMotPossible:
            st.write(mot)
    else:
        st.write("Aucune solution")

def main():
    solvermode = st.sidebar.checkbox('Solver mode')
    if solvermode:
        solver()
    else:
        gamemode()

main()