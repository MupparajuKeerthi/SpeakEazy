




async function getvideo() {
    try {
        const res = await fetch("http://127.0.0.1:5000/mupparaju", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ mupparaju: 'Start' })
        });
        if (!res.ok) {
            throw new Error("You Failed");
        }
    } catch (error) {
        console.error(error);
    }
}

document.getElementById('9876654').addEventListener('click', getvideo);
