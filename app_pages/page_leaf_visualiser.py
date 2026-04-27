import streamlit as st


def page_leaf_visualiser_body():

    st.title("Leaf Visualiser")

    st.write(
        "This page presents a visual study to differentiate healthy cherry leaves "
        "from those affected by powdery mildew."
    )
    
    st.info("Expand each section below to see the visuals.")

    with st.expander("Show Average Images"):
        st.header("Average Images")
        col1, col2 = st.columns(2)

        with col1:
            st.image("outputs/plots/avg_healthy.png", caption="Average Healthy Leaf")

        with col2:
            st.image("outputs/plots/avg_mildew.png", caption="Average Powdery Mildew Leaf")

        st.write(
            "The average images highlight differences in colour and texture. "
            "Powdery mildew leaves show lighter, patchy regions compared to healthy leaves."
        )

    with st.expander("Show Variability Images"):
        st.header("Variability Images")
        col1, col2 = st.columns(2)

        with col1:
            st.image("outputs/plots/var_healthy.png", caption="Variability Healthy")

        with col2:
            st.image("outputs/plots/var_mildew.png", caption="Variability Mildew")

        st.write(
            "Variability images show how pixel values differ across samples. "
            "Higher variability in mildew leaves suggests irregular patterns caused by infection."
        )

    with st.expander("Show Difference Image"):
        st.header("Difference Between Average Images")
        st.image("outputs/plots/difference.png", caption="Difference Image")

        st.write(
            "The difference image highlights regions where healthy and mildew leaves diverge, "
            "confirming that visual features can distinguish between classes."
        )

    with st.expander("Show Image Montage"):
        st.header("Image Montage")
        col1, col2 = st.columns(2)

        with col1:
            st.image("outputs/plots/montage_healthy.png", caption="Healthy Leaves")

        with col2:
            st.image("outputs/plots/montage_mildew.png", caption="Mildew Leaves")

        st.write(
            "The montage shows sample images from each class. "
            "Mildew leaves display visible white fungal patterns, while healthy leaves are uniformly green."
        )

    st.header("Conclusion")
    st.write(
        "The visual analysis confirms that healthy and powdery mildew leaves can be distinguished "
        "based on colour, texture, and visible fungal patterns. "
        "This supports the business requirement for visual differentiation."
    )