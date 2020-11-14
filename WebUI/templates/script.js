var years = prompt('Ввыедите ваш логин?', 'NonAuthorized');



$('#send-message').on('submit', function (event) {
    event.preventDefault();
    var message = $('.messages-me').first().clone();
    message.find('p').text($('#input-me').val());
    let client_meesage = $('#input-me').val();
    // console.log(client_meesage)
    $('#input-me').val('');
    message.appendTo('.messages-list');

    var messagee = $('.messages-you').first().clone();
    let my_post = $.ajax({
      url: 'http://localhost:5000/ai-quotes',
      type: "POST",
      data: {"id": 11, "author": years,
        "quote": client_meesage},
    });
    // let my_get = $.ajax({
    //   url: 'http://localhost:5000/ai-quotes',
    //   type: "GET",
    // });
    function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
    }

    readTextFile("frame.json", function(text){
    var data = JSON.parse(text);

        let bot_message;
        let answ_message;
        for (let i = 0; i < 550; i++) {
            let str = data[i]['Обращение']
            // console.log(client_meesage)
            // console.log(str.indexOf(client_meesage))
            if (str.indexOf(client_meesage) !== -1) {
                bot_message = data[i]['Ссылка']
                console.log(bot_message)
                answ_message = "Я нашел для вас ответ\n" + bot_message
                break;
            }

        if (bot_message !== undefined){
        answ_message = "Я нашел для вас ответ" + bot_message
        } else {
            answ_message = "Попобуйте обратиться в тех поддержду, на данный момент у меня нет ответа на ваш вопрос."
        }
        }

    messagee.find('p').text(answ_message);
    messagee.appendTo('.messages-list');
    });

});
