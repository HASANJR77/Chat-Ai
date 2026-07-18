const chat = document.getElementById("chat");
const input = document.getElementById("message");
const send = document.getElementById("send");

function mesajEkle(mesaj, sinif) {
    const div = document.createElement("div");
    div.className = sinif;
    div.textContent = mesaj;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

send.onclick = async function () {

    const mesaj = input.value.trim();

    if (mesaj === "") return;

    mesajEkle(mesaj, "user");
    input.value = "";

    try {

        const cevap = await fetch("http://192.168.1.106:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: mesaj
            })
        });

        const veri = await cevap.json();

        mesajEkle(veri.reply, "ai");

    } catch (e) {

        mesajEkle("Sunucuya bağlanılamadı.", "ai");

    }

}

input.addEventListener("keydown", function(e){
    if(e.key==="Enter"){
        send.click();
    }
});