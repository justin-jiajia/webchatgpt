const qu = document.getElementById('chatquestion');
const box = document.getElementById('chatbox');
document.getElementById('send').onclick = () => {
    const que = qu.value;
    var nn = document.createElement('p');
    nn.setAttribute('class', 'from-me');
    nn.innerText = que;
    box.appendChild(nn);
    //
    nn = document.createElement('p');
    nn.setAttribute('class', 'from-them');
    box.appendChild(nn);
    fetch('/ask/', { method: 'POST', body: JSON.stringify({ question: que }) }).then((res) => {
        res.json().then((res) => {
            if (!res.suc) {
                nn.innerHTML = '<strong>出错了！</strong>';
            } else {
                id = res.id;
                function f(id) {
                    setTimeout(() => {
                        fetch('/ans/', { method: 'POST', body: JSON.stringify({ id: id }) }).then((res) => {
                            res.json().then((res) => {
                                if (!res.suc) {
                                    nn.innerHTML = '<strong>出错了！</strong>';
                                } else {
                                    nn.innerText = res.ans;
                                    if (!res.finish) f(id);
                                }
                            })
                        });
                    }, 500);
                }
                f(id);
            }
        })
    });
};