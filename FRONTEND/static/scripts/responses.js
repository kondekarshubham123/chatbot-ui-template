async function getBotResponse(input){
    // 'http://localhost:8080/api/chatbot/talk'
    // 'http://localhost:8080/api/chatbot/check'
    // console.log(input);
    const getResponse = async () => {
        const response = await fetch('https://chatbot-backe.herokuapp.com/api/chatbot/talk',{
          method: 'POST',
          headers: {
              "content-type": "application/json",
              "Access-Control-Allow-Origin": "*",
          },
          body: JSON.stringify({talk: input})
        });
        myJson = await response.json();
        return myJson;
    }

    
    const data = await getResponse();
    console.log(typeof(data["Message"]));
    return data["Message"];
}