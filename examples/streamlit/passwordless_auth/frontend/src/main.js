import {Streamlit} from "streamlit-component-lib"

async function loadPasswordlessScript(document) {
    if (document.getElementById("passwordless_script")) {
        return;
    }
    const script = document.createElement('script');
    script.src = 'https://cdn.passwordless.dev/dist/1.1.0/umd/passwordless.umd.min.js';
    script.crossorigin = 'anonymous';
    script.id = "passwordless_script"
    const scriptLoading = new Promise(resolve => {
        script.onload = () => {
            resolve();
        }
    });
    document.head.appendChild(script);
    await scriptLoading;
}

async function onRender(event) {
    try {
        await loadPasswordlessScript(parent.document);

        const detail = event.detail

        console.log(detail);
        console.log(detail.args);

        const data = detail.args["data"]

        console.log(data);

        const config = {
            apiUrl: data["api_url"],
            apiKey: data["api_key"]
        }

        const client = new parent.window.Passwordless.Client(config)

        if (data['type'] === 'register') {
            const {token, error} = await client.register(data["token"])

            console.log(token)
            console.log(error)

            Streamlit.setComponentValue({
                token: token,
                error: error
            })
        } else if (data['type'] === 'login') {

            const {token, error} = await client.signinWithAlias(data["alias"])

            console.log(token)
            console.log(error)

            Streamlit.setComponentValue({
                token: token,
                error: error
            })
        }

    } catch (e) {
        console.log(e);

        Streamlit.setComponentValue({
            exception: e.message
        })
    }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()