import streamlit as st
import numpy as np
import time


def random_number_generator():

    st.header("🔢 Random Number Generator")
    st.write("Generate a random number with an animated rolling effect!")

    # -----------------------------
    # MIN & MAX
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        min_number = st.number_input(
            "Minimum Number",
            value=1,
            step=1
        )

    with col2:
        max_number = st.number_input(
            "Maximum Number",
            value=100,
            step=1
        )

    # -----------------------------
    # SECRET NUMBER
    # -----------------------------
    st.subheader("🔐 Secret Number")

    secret_input = st.text_input(
        "Enter Secret Number",
        value="25",
        type="password"
    )

    st.caption("🔒 Your secret number is hidden")

    # -----------------------------
    # GENERATE
    # -----------------------------
    if st.button("🎲 Generate Number", use_container_width=True):

        # Check range
        if min_number >= max_number:
            st.error(
                "❌ Minimum number must be smaller than maximum number!"
            )
            return

        # Convert secret number
        try:
            secret_number = int(secret_input)
        except ValueError:
            st.error("❌ Please enter a valid secret number!")
            return

        # Check secret number range
        if secret_number < min_number or secret_number > max_number:
            st.error(
                f"❌ Secret number must be between "
                f"{int(min_number)} and {int(max_number)}!"
            )
            return

        # -----------------------------
        # ANIMATION
        # -----------------------------
        placeholder = st.empty()

        for _ in range(25):

            random_number = np.random.randint(
                int(min_number),
                int(max_number) + 1
            )

            # NO HTML HERE
            with placeholder.container():
                st.info("🎰 GENERATING...")
                st.markdown(f"# 🎯 {random_number}")

            time.sleep(0.08)

        # -----------------------------
        # FINAL NUMBER
        # -----------------------------
        final_number = np.random.randint(
            int(min_number),
            int(max_number) + 1
        )

        placeholder.empty()

        # -----------------------------
        # FINAL RESULT
        # -----------------------------
        st.subheader("🎉 Final Result")

        st.markdown(f"# 🎯 {final_number}")

        # -----------------------------
        # WIN / LOSE
        # -----------------------------
        if final_number == secret_number:

            st.success(
                "🏆 CONGRATULATIONS! YOU WIN! 🎉"
            )

            st.write(
                f"The generated number **{final_number}** "
                f"matched your secret number!"
            )

            st.balloons()

        else:

            st.warning(
                "😅 BETTER LUCK NEXT TIME!"
            )

            st.write(
                f"The generated number **{final_number}** "
                "did not match your secret number."
            )