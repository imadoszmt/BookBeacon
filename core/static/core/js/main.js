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
    const signInFields = document.getElementById('signInFields');
    const signUpFields = document.getElementById('signUpFields');

    if (isSignUp) {
        title.textContent = 'Sign Up';
        submitButton.textContent = 'Sign Up';
        switchText.innerHTML = 'Already have an account? <a href="signin/" onclick="switchAuthMode()">Sign in</a>';
        signInFields.classList.add('hide');
        signUpFields.classList.remove('hide');
    } else {
        title.textContent = 'Sign In';
        submitButton.textContent = 'Sign In';
        switchText.innerHTML = 'Don\'t have an account? <a href="signup/" onclick="switchAuthMode()">Sign up</a>';
        signInFields.classList.remove('hide');
        signUpFields.classList.add('hide');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('authForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        formData.append('action', isSignUp ? 'signup' : 'signin');

        fetch('/auth/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                closeAuthModal();
                location.reload();  // Reload the page to reflect the logged-in state
            } else {
                // Display errors
                const errorMessages = Object.values(data.errors).flat();
                alert(errorMessages.join('\n'));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
});
