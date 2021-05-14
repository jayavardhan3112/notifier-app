const axios = require('axios');
const alert = require('alert'); 
const twilio = require('twilio');
const emailjs = require('emailjs');

const sendMessage = false;
const interval = 60000*3;
const clientID = 'AC10cf265a76cdc96a52d5fc75317ad90e';
const clientSec = 'e1f41822f7b3b21fbcad599d65f1f463';
const reservedString = 'Computer Science MCS, Computer Science MS, Software Engineering MS, Robotics and Autonomous Systems (AI) MS, Computer Engineering MS student with 1-3 courses completed or in progress';

const nonReservedString = 'Non Reserved Available Seats: ';
const dataminingUrl_78726  = "https://webapp4.asu.edu/catalog/CourseDrawer.ext?sp=SCSE&sp=S572&sp=STEMPE&sp=S2217&sp=SCOORL1-74&sp=S104264&sp=ZH4sIAAAAAAAAAFvzloG1uIhBJCuxLFEvN7EkQ88pM90lNTkzNzEn5Lho%2BM9GDX9mBiZPoKrkxJxUHwa2zLySsMScEgYxH5AefZAefaAez7yS1PTUIuuKIgYBsGE5iXnpen6luUmpRW1rpspyT3nQzcTAUFHAAAQYNkJ19%2FyZL7%2FS%2BrcsMwObJwNHUmaJc35pXoknAyeQ6ZOal16S4ckgnJZZVFzil59XlVqU71RZkgq0w5OBJye%2FPLW4JDi1xCkTqIGtODM9rzQ3moEzNzE9L7OkNCW1hIEp2qmikKGOgek%2FAvwDYaCLGEuLQPJrPov%2FYOMIeQBzKTOjcVtFBQDynhK0JQEAAA%3D%3D&sp=STEMPE";
const dataminingUrl_85504  = "https://webapp4.asu.edu/catalog/CourseDrawer.ext?sp=SCSE&sp=S572&sp=STEMPE&sp=S2217&sp=SCOORL1-74&sp=S104264&sp=ZH4sIAAAAAAAAAFvzloG1uIhBJCuxLFEvN7EkQ88pM90lNTkzNzEn5Lho%2BM9GDX9mBiZPoKrkxJxUHwa2zLySsMScEgYxH5AefZAefaAez7yS1PTUIuuKIgYBsGE5iXnpen6luUmpRW1rpspyT3nQzcTAUFHAAAQYNkJ19%2FyZL7%2FS%2BrcsMwObJwNHUmaJc35pXoknAyeQ6ZOal16S4ckgnJZZVFzil59XlVqU71RZkgq0w5OBJye%2FPLW4JDi1xCkTqIGtODM9rzQ3moEzNzE9L7OkNCW1hIEp2qmikKGOgek%2FAvwDYaCLGEuLQPJrPov%2FYOMIeQBzKTOjH0NFBQCBgf%2FIJQEAAA%3D%3D&sp=STEMPE";
const aiUrl = "https://webapp4.asu.edu/catalog/CourseDrawer.ext?sp=SCSE&sp=S571&sp=STEMPE&sp=S2217&sp=SCOORL1-74&sp=S104263&sp=ZH4sIAAAAAAAAAFvzloG1uIhBJCuxLFEvN7EkQ88pM90lNTkzNzEn5Lho%2BM9GDX9mBiZPoKrkxJxUHwa2zLySsMScEgYxH5AefZAefaAez7yS1PTUIuuKIgYBsGE5iXnpen6luUmpRW1rpspyT3nQzcTAUFHAAAQYNkJ19%2FyZL7%2FS%2BrcsMwObJwNHUmaJc35pXoknAyeQ6ZOal16S4ckgnJZZVFzil59XlVqU71RZkgq0w5OBJye%2FPLW4JDi1xCkTqIGtODM9rzQ3moEzNzE9L7OkNCW1hIEp2qmikKGOgek%2FAvwDYaCLGEuLQPJrPov%2FYOMIeQBzKTNjbH1FBQCdVv7VJQEAAA%3D%3D&sp=STEMPE";
const mobileComputingUrl = "https://webapp4.asu.edu/catalog/CourseDrawer.ext?sp=SCSE&sp=S535&sp=STEMPE&sp=S2217&sp=SLSE104&sp=S104251&sp=ZH4sIAAAAAAAAAFvzloG1uIhBJCuxLFEvN7EkQ88pM90lNTkzNzEn5Lho%2BM9GDX9mBiZPoKrkxJxUHwa2zLySsMScEgYxH5AefZAefaAez7yS1PTUIuuKIgYBsGE5iXnpen6luUmpRW1rpspyT3nQzcTAUFHAAAQYNkJ19%2FyZL7%2FS%2BrcsMwObJwNHUmaJc35pXoknAyeQ6ZOal16S4ckgnJZZVFzil59XlVqU71RZkgq0w5OBJye%2FPLW4JDi1xCkTqIGtODM9rzQ3moEzNzE9L7OkNCW1hIEp2qmikKGOgek%2FAvwDYaCLGEuLQPJrPov%2FYOMIeQBzKTOj5rOKCgAp4mHDJQEAAA%3D%3D&sp=STEMPE";
const SMLUrl = "https://webapp4.asu.edu/catalog/CourseDrawer.ext?sp=SCSE&sp=S575&sp=STEMPE&sp=S2217&sp=SCAVC351&sp=S125131&sp=ZH4sIAAAAAAAAAFvzloG1uIhBJCuxLFEvN7EkQ88pM90lNTkzNzEn5Lho%2BM9GDX9mBiZPoKrkxJxUHwa2zLySsMScEgYxH5AefZAefaAez7yS1PTUIuuKIgYBsGE5iXnpen6luUmpRW1rpspyT3nQzcTAUFHAAAQYNkJ19%2FyZL7%2FS%2BrcsMwObJwNHUmaJc35pXoknAyeQ6ZOal16S4ckgnJZZVFzil59XlVqU71RZkgq0w5OBJye%2FPLW4JDi1xCkTqIGtODM9rzQ3moEzNzE9L7OkNCW1hIEp2qmikKGOgek%2FAvwDYaCLGEuLQPJrPov%2FYOMIeQBzKTOj6fWKCgCphQf8JQEAAA%3D%3D&sp=STEMPE";
const courseUrls = [dataminingUrl_78726, dataminingUrl_85504, aiUrl, mobileComputingUrl, SMLUrl]
count = 0;
const stopInterval = () => {
	const today2 = new Date();
	const time2 = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
 	clearInterval(dataminingFunction);
  	console.log(`ended script at ${time2}`);
}

function sendEmail() {
	const client = new emailjs.SMTPClient({
		Host : "Smtp.Gmail.com",
        Port : 587,
        EnableSsl : true,
        Timeout : 10000,
        UseDefaultCredentials : false,
        Credentials : new NetworkCredential("jayavardhan3112@mail.com", )
	});
	client.send(
		{
			text: 'i hope this works',
			from: 'jayavardhan3112@gmail.com',
			to: 'jayavardhan3112@gmail.com',
			cc: 'jayavardhan3112@gmail.com',
			subject: 'testing emailjs',
		},
		(err, message) => {
			console.log(err || message);
		}
	);
}


async function datamining() {
	var client = new twilio(clientID, clientSec);
	const res = await axios.post(dataminingUrl_78726);
	const res2 = await axios.post(dataminingUrl_85504);
	const res3 = await axios.post(aiUrl);
	const res4 = await axios.post(SMLUrl);
	const data = res.data;
	const data2 = res2.data;
	const data3 = res3.data;
	const data4 = res4.data;
	const specificData = data.substring(data.indexOf(reservedString), data.indexOf(reservedString) + 240);
	const fullData = data.substring(data.indexOf(nonReservedString));
	const finalFullData = fullData.substring(0, fullData.indexOf("\n"))
	const finalSpecificData = specificData.replace("</span></td>", "").replace("\t", "").replace("\n", "").replace('<td class="rc"> <span>', "")
	const specificData2 = data2.substring(data2.indexOf(reservedString), data2.indexOf(reservedString) + 240);
	const fullData2 = data2.substring(data2.indexOf(nonReservedString));
	const finalFullData2 = fullData2.substring(0, fullData2.indexOf("\n"))
	const finalSpecificData2 = specificData2.replace("</span></td>", "").replace("\t", "").replace("\n", "").replace('<td class="rc"> <span>', "")
	const specificData3 = data3.substring(data3.indexOf(reservedString), data3.indexOf(reservedString) + 240);
	const fullData3 = data3.substring(data3.indexOf(nonReservedString));
	const finalFullData3 = fullData3.substring(0, fullData3.indexOf("\n"))
	const finalSpecificData3 = specificData3.replace("</span></td>", "").replace("\t", "").replace("\n", "").replace('<td class="rc"> <span>', "")
	const specificData4 = data4.substring(data4.indexOf(reservedString), data3.indexOf(reservedString) + 240);
	const fullData4 = data4.substring(data4.indexOf(nonReservedString));
	const finalFullData4 = fullData4.substring(0, fullData4.indexOf("\n"))
	const finalSpecificData4 = specificData4.replace("</span></td>", "").replace("\t", "").replace("\n", "").replace('<td class="rc"> <span>', "")
	// console.log("DATAMINING")
	if (finalFullData.replace(nonReservedString,"") === '0' && finalSpecificData.replace(reservedString, "").trim().replace(/(\r\n|\n|\r)/g,"") === '0') {
		// console.log("leave Datamining 78726 Class");
	} else {
		const text = "Book Datamining 78726 class asap"
		alert(text)
		if(sendMessage) {
			await client.messages.create({
			  to: '+919553533511',
			  from: '+13126355164',
			  body: text
			});
		}
		stopInterval()

	}
	// console.log("DATAMINING")
	if (finalFullData2.replace(nonReservedString,"") === '0' && finalSpecificData2.replace(reservedString, "").trim().replace(/(\r\n|\n|\r)/g,"") === '0') {
		// console.log("leave Datamining 85504 Class");
	} else {
		const text = "Book Datamining 85504 class asap"
		alert(text)
		if(sendMessage) {
			await client.messages.create({
			  to: '+919553533511',
			  from: '+13126355164',
			  body: text
			});
		}
		stopInterval()
	}

	// console.log("AI")
	if (finalFullData3.replace(nonReservedString,"") === '0' && finalSpecificData3.replace(reservedString, "").trim().replace(/(\r\n|\n|\r)/g,"") === '0') {
		// console.log("leave AI Class")
	} else {
		const text = "Book AI class asap"
		alert(text)
		if(sendMessage) {
			await client.messages.create({
			  to: '+919553533511',
			  from: '+13126355164',
			  body: text
			});
		}
		stopInterval()
	}

	// console.log("SML")
	if (finalFullData4.replace(nonReservedString,"") === '0' && finalSpecificData4.replace(reservedString, "").trim().replace(/(\r\n|\n|\r)/g,"") === '0') {
		// console.log("leave SML Class");
	} else {
		const text = "Book Statistical Machine Learning class asap"
		alert(text)
		if(sendMessage) {
			await client.messages.create({
			  to: '+919553533511',
			  from: '+13126355164',
			  body: text
			});
		}
		stopInterval()
	}

	count++;
	const text = count>1 ? "times" : "time";
	console.clear();
	var today = new Date();
	var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
	console.log(`CHECKED -> ${count} ${text}, Last checked at ${time}`)
}

const dataminingFunction = setInterval(datamining, interval);
var today = new Date();
var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
console.log(`started script at ${time}`);
datamining();
