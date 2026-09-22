import streamlit as st
import random
import time


def coin_flip():

    st.header("🪙 Coin Flip")
    st.write("Flip the coin and watch it spin before it lands!")

    if st.button("🪙 FLIP COIN", use_container_width=True):

        placeholder = st.empty()

        # Coin animation frames
        frames = [
            "🪙",
            "🔵",
            "🪙",
            "🔵",
            "🪙",
            "🔵",
            "🪙",
            "🔵",
        ]

        # --------------------------------
        # FLIPPING ANIMATION
        # --------------------------------

        for _ in range(4):

            for frame in frames:

                with placeholder.container():

                    st.info("🌀 FLIPPING...")

                    st.markdown(
                        f"# {frame}"
                    )

                    st.caption("The coin is spinning...")

                time.sleep(0.08)

        # --------------------------------
        # SLOW DOWN
        # --------------------------------

        for frame in ["🔵", "🪙", "🔵", "🪙"]:

            with placeholder.container():

                st.warning("🌀 ALMOST THERE...")

                st.markdown(
                    f"# {frame}"
                )

                st.caption("The coin is about to land...")

            time.sleep(0.18)

        # --------------------------------
        # FINAL RESULT
        # --------------------------------

        result = random.choice(["HEADS", "TAILS"])

        placeholder.empty()

        st.success("🎉 COIN LANDED!")

        if result == "HEADS":

            st.markdown("# 👑 HEADS!")

        else:

            st.markdown("# 🪙 TAILS!")

        st.balloons()

        st.caption("✨ The coin has landed!")