var axios = require('axios');

var upvotePrediction = (token, match_id, prediction_id) => {
  // Description: Upvotes the given prediction
	// Endpoint `POST /v1/matches/:match_id/predictions/:prediction_id/upvote/`
  console.log('working')
	// Response: 200
  axios.post(`http://api.tahmin.io/v1/matches/${match_id}/predictions/${prediction_id}/undoupvote/`,{}, {
    headers: 
    {
      Authorization: `Token ${token}`
    }
  })
    .then(response => {
      console.log(response.data)
      // upvote the message and render to the same page
    })
			.catch(err => console.log(err));

};
upvotePrediction("d2fd1d30641a7a0b839ea4565f06f654456236fe", 75835 ,1240)