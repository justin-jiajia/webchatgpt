var id = -1;
const qu = document.getElementById('chatquestion');
const box = document.getElementById('chatbox');
document.getElementById('send').onclick = function () {
    const que = qu.value;
    const xmlHttp = new XMLHttpRequest();
    xmlHttp.open('POST', '/ask', true);
    xmlHttp.send(JSON.stringify({ 'question': que }));
    id++;
    var nn = document.createElement('p');
    nn.setAttribute('class', 'from-me');
    nn.innerText = que;
    box.appendChild(nn);
    //
    nn=document.createElement('p');
    nn.setAttribute('class', 'from-them');
    box.appendChild(nn);
    const timer = window.setInterval(function () {
        if (xmlHttp.readyState == XMLHttpRequest.DONE) {
            nn.innerHTML = xmlHttp.responseText.replace(que, '');
            window.clearTimeout(timer);
        }
        //console.log(xmlHttp.responseText);
        nn.innerText = xmlHttp.responseText.replace(que, '');
        //nn.innerHTML = nn.innerHTML;
    }, 100);
};