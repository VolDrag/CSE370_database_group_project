from app import create_app  # Import the 'create_app' function from the _init_.py file

app = create_app()  # Create the app using the factory function

if __name__ == "_main_":  # This ensures that the app runs only if this file is executed directly
    app.run(debug=True)  # Run the app with debug mode enabled