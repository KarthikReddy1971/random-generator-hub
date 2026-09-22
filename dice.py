import streamlit as st
import random
import time


def dice_roller():

    st.header("🎲 Dice Roller")
    st.write("Roll the dice and watch the result appear!")

    number_of_dice = st.selectbox(
        "Choose number of dice",
        [1, 2, 3, 4, 5, 6]
    )

    if st.button("🎲 Roll Dice", use_container_width=True):

        placeholder = st.empty()

        dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

        # Rolling animation
        for _ in range(15):

            temporary_dice = [
                random.randint(1, 6)
                for _ in range(number_of_dice)
            ]

            dice_display = "   ".join(
                dice_faces[x - 1]
                for x in temporary_dice
            )

            placeholder.markdown(
                f"""
                <div style="
                    text-align:center;
                    padding:30px;
                    border-radius:20px;
                    background:#ff9966;
                    color:white;
                ">
                    <h2>🎲 ROLLING...</h2>
                    <div style="font-size:80px;">
                        {dice_display}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.12)

        # Final result
        final_dice = [
            random.randint(1, 6)
            for _ in range(number_of_dice)
        ]

        total = sum(final_dice)

        final_display = "   ".join(
            dice_faces[x - 1]
            for x in final_dice
        )

        # Clear animation
        placeholder.empty()

        # Final result using Streamlit
        st.success("🎉 DICE RESULT")

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:25px;
                border-radius:20px;
                background:#f0f2f6;
            ">
                <div style="font-size:80px;">
                    {final_display}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h1 style='text-align:center;'>🎯 Total: {total}</h1>",
            unsafe_allow_html=True
        )