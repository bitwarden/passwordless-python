import {Streamlit} from "streamlit-component-lib"
import {Client} from "@passwordlessdev/passwordless-client";

async function onRender(event) {
    try {
        const detail = event.detail

        console.log(detail);
        console.log(detail.args);

        const data = detail.args["data"]

        console.log(data);

        const client = new Client({
            apiUrl: data["api_url"],
            apiKey: data["api_key"],
        })

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