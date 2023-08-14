const url = 'https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=Seattle';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '273fcc3ee5msh1d73973e653170fp1088fdjsnacaf4a62c866',
		'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
	}
};

fetch (url, options)
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(err => console.error(err));