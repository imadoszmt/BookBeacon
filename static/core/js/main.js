let isSignUp = false;

function openAuthModal() {
    document.getElementById('authModal').style.display = 'block';
}

function closeAuthModal() {
    document.getElementById('authModal').style.display = 'none';
}

function switchAuthMode() {
    isSignUp = !isSignUp;
    const title = document.getElementById('authTitle');
    const submitButton = document.getElementById('authSubmit');
    const switchText = document.getElementById('authSwitch');

    if (isSignUp) {
        title.textContent = 'Sign Up';
        submitButton.textContent = 'Sign Up';
        switchText.innerHTML = 'Already have an account? <a href="" onclick="switchAuthMode()">Sign in</a>';
    } else {
        title.textContent = 'Sign In';
        submitButton.textContent = 'Sign In';
        switchText.innerHTML = 'Don\'t have an account? <a href="#" onclick="switchAuthMode()">Sign up</a>';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('authForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (isSignUp) {
            console.log('Sign up with:', email, password);
            // Here you would typically make an API call to register the user
        } else {
            console.log('Sign in with:', email, password);
            // Here you would typically make an API call to authenticate the user
        }

        closeAuthModal();
    });
});
