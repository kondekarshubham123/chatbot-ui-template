function getBotResponse(input){
    // 'http://localhost:8080/api/chatbot/talk'
    // 'http://localhost:8080/api/chatbot/check'
    // console.log(input);
    // const myBody = {"talk": input };
    // const getResponse = async () => {
    //     const response = await fetch('http://localhost:8080/api/chatbot/talk', {
    //       method: 'POST',
    //       data: JSON.stringify(myBody),
    //       headers: {
    //         'Access-Control-Allow-Origin': '*',
    //         'Access-Control-Allow-Methods': 'GET, POST',
    //         'Access-Control-Allow-Headers': 'Content-Type',
    //         'Access-Control-Max-Age': '3600'
    //       }
    //     });
    //     const myJson = await response.json();
    //     console.log(myJson);
    //     // return myJson["Working"];
    // }

    
    // getResponse().then((data) => {
    //   console.log(data);
    // });
    
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}