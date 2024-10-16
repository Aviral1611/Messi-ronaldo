import pandas as pd
import plotly_express as px
import streamlit as st



st.set_page_config(page_title="Football",page_icon=":wave:",layout="wide")



df = pd.read_excel(
    io='MessiRonaldo.xlsx',
   
)




st.header("Analysis of Messi and Ronaldo's Season till their time in LA LIGA including the champions league stats!")



if 'selected_players' not in st.session_state:
    st.session_state.selected_players = df["Player"].unique()

if 'selected_seasons' not in st.session_state:
    st.session_state.selected_seasons = df["Season"].unique()

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar filters
st.sidebar.markdown("[**Messi**](messi.py)")
st.sidebar.header("Please filter here:")
selected_players = st.sidebar.multiselect(
    "Select the player:",
    options=df["Player"].unique(),
    default=st.session_state.selected_players,  # Use session state
    key='players_filter'  # Unique key for the widget to store state
)

selected_seasons = st.sidebar.multiselect(
    "Select the season:",
    options=df["Season"].unique(),
    default=st.session_state.selected_seasons,  # Use session state
    key='seasons_filter'  # Unique key for the widget to store state
)

# Update session state on change
st.session_state.selected_players = selected_players
st.session_state.selected_seasons = selected_seasons

# Filter data based on selections
df_selection = df.query(
    "Player == @selected_players & Season == @selected_seasons"
)

# Display filtered data
st.dataframe(df_selection)


st.title(":bar_chart: Football Dashboard")
st.markdown("##")

total_ll_goals = int(df_selection["Liga_Goals"].sum())
total_cl_goals = int(df_selection["CL_Goals"].sum())
total_ll_asis = int(df_selection["Liga_Asts"].sum())
total_cl_asis = int(df_selection["CL_Asts"].sum())

left_column, middle_column , right_column, right1_column = st.columns(4)
with left_column:
    st.subheader("Total la liga Goals")
    st.subheader(f"Goals: {total_ll_goals:,}")

with middle_column:
    st.subheader("Total Champions League Goals")
    st.subheader(f"Goals: {total_cl_goals:,}")

with right_column:
    st.subheader("Total Champions league assists")
    st.subheader(f"Assists:{total_cl_asis:,}")

with right1_column:
    st.subheader("Total la liga assists")
    st.subheader(f"Assists:{total_ll_asis:,}")

st.markdown("---")

if not selected_players or not selected_seasons:
    st.write("Please select at least one player and one season to view the analysis.")
else:
    # Check if df_selection is empty after filtering
    if df_selection.empty:
        st.write("No data available for the selected filters.")
    else:
        # Proceed with calculating top goals and assists
        top_goals = df_selection.loc[df_selection['Liga_Goals'].idxmax()]
        top_assists = df_selection.loc[df_selection['Liga_Asts'].idxmax()]

        st.write(f"**Top Goal Scoring Season**: {top_goals['Player']} in {top_goals['Season']} with {top_goals['Liga_Goals']} La Liga goals.")
        st.write(f"**Top Assisting Season**: {top_assists['Player']} in {top_assists['Season']} with {top_assists['Liga_Asts']} La Liga assists.")

st.markdown("---")

st.subheader("Historical Milestones")

milestone_goals = df.groupby("Player").apply(lambda x: x.loc[x["Liga_Goals"].idxmax()])
milestone_assists = df.groupby("Player").apply(lambda x: x.loc[x["Liga_Asts"].idxmax()])

st.write("### Highest Goal Seasons")
st.table(milestone_goals[['Player', 'Season', 'Liga_Goals', 'CL_Goals']])

st.write("### Highest Assist Seasons")
st.table(milestone_assists[['Player', 'Season', 'Liga_Asts', 'CL_Asts']])

st.markdown("---")

hide_st_style = """
<style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  
  
  </style>
"""

st.subheader("Goals Comparison per Season")

fig_goals = px.bar(
    df_selection,
    x="Season",
    y=["Liga_Goals", "CL_Goals"],
    color="Player",
    barmode="group",
    title="Goals per Season in La Liga and Champions League",
    labels={"value": "Goals", "variable": "Competition"},
)
st.plotly_chart(fig_goals, use_container_width=True)

st.subheader("Goals Progression Over Seasons")

fig_line = px.line(
    df_selection,
    x="Season",
    y=["Liga_Goals", "CL_Goals"],
    color="Player",
    markers=True,
    title="Goals Progression in La Liga and Champions League",
    labels={"value": "Goals", "variable": "Competition"},
)
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("Goals vs Assists Distribution")

fig_pie = px.pie(
    df_selection,
    names=["Liga_Goals", "Liga_Asts", "CL_Goals", "CL_Asts"],
    values=[total_ll_goals, total_ll_asis, total_cl_goals, total_cl_asis],
    title="Goals vs Assists in La Liga and Champions League",
)
st.plotly_chart(fig_pie, use_container_width=True)





# Custom CSS to hide Streamlit menu and footer
hide_st_style = """
<style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)