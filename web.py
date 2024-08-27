import streamlit as st
import functions

# Initialize session state for todos if not already set
if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state.new_todo.strip()
    if new_todo:
        st.session_state.todos.append(new_todo + "\n")
        functions.write_todos(st.session_state.todos)
        st.session_state.new_todo = ""  # Clear the input field

def remove_todo(index):
    st.session_state.todos.pop(index)
    functions.write_todos(st.session_state.todos)
    st.session_state.success_message = "Congratulations on completing your task!"

# Streamlit app layout
st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centering the title, subtitle, and description
st.markdown('<div class="centered-text">', unsafe_allow_html=True)
st.title("Task Ninja 📝")
st.subheader("Tame your to-dos before they run wild!")
st.write("Conquer Your Day, One Task at a time 🔪🔪🔪")
st.markdown('</div>', unsafe_allow_html=True)

# Create a list of todo checkboxes
checkboxes = []
for index, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    checkboxes.append(checkbox)

# Check if any checkbox is selected to remove the corresponding todo
for index, checked in enumerate(checkboxes):
    if checked:
        remove_todo(index)
        # After removing, break out of the loop to avoid issues with index changes
        break

# Display success message if set
if "success_message" in st.session_state:
    st.success(st.session_state.success_message)
    del st.session_state.success_message  # Clear the message after displaying

# Text input for adding new todos
st.text_input(
    label="Add new Todo...",
    placeholder="Type here...",
    on_change=add_todo,
    key="new_todo"
)
