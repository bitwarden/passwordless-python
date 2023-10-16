async function handleSigninClick(e) {
    e.preventDefault();
    const alias = document.getElementById("alias").value;

    Status("Starting sign in...");

    /**
     * Initiate the Passwordless client with your public api key
     */
    const p = new Passwordless.Client({
        apiUrl: API_URL,
        apiKey: API_KEY
    });

    try {
        /**
         * Sign in - The Passwordless API and the browser initiates a sign in based on the alias
         */

            //var userId = await fetch("user/id").then(r => r.json()); // get user id from database

        const {token, error} = await p.signinWithAlias(alias);
        //const token = await p.signinWithId(486761564);
        if (error) {
            Status(JSON.stringify(error, null, 2));
            Status("Sign in failed, received the following error");
            return;
        }

        console.log("Received token", token);
        /**
         * Verify the sign in - Call your backend to verify the token created from the sign in
         */

        const response = await fetch("/passwordless/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                token: token
            })
        });

        const user = await response.json();

        /**
         * Done - you can now check the user result for status, userid etc
         */
        Status("User details: " + JSON.stringify(user, null, 2));
        Status("Yey! Succesfully signed in without a password!");

        console.log("User", user);
    } catch (e) {
        console.error("Things went really bad: ", e);
        Status("Things went bad, check console");
    }
}

document
    .getElementById("passwordless-signin")
    .addEventListener("click", handleSigninClick);
