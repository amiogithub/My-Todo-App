import streamlit as st
import functions

# Initialize session state for todos if not already set
if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()

def add_todo():
    """Add a new todo to the list."""
    new_todo = st.session_state.new_todo.strip()
    if new_todo:
        st.session_state.todos.append(new_todo + "\n")
        functions.write_todos(st.session_state.todos)
        st.session_state.new_todo = ""  # Clear the input field

def remove_todo(index):
    """Remove a todo from the list.""
    st.session_state.todos.pop(index)
    functions.write_todos(st.session_state.todos)

# Streamlit app layout
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Create a list of todo checkboxes
checkboxes = []
for index, todo in enumerate(st.session_state.todos):
    # Use a unique key for each checkbox
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    checkboxes.append(checkbox)

# Check if any checkbox is selected to remove the corresponding todo
for index, checked in enumerate(checkboxes):
    if checked:
        remove_todo(index)
        # After removing, break out of the loop to avoid issues with index changes
        break

# Text input for adding new todos
st.text_input(
    label="Add new Todo...",
    placeholder="Type here...",
    on_change=add_todo,
    key="new_todo"
)
