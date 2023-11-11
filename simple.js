const puppeteer = require('puppeteer');

(async()=>{

	const browser = await puppeteer.launch({headless:false})
	const page = await browser.newPage()
	await page.goto('https://www.youtube.com/@Illya.Landar/videos')

	let arr = await page.evaluate(()=>{

		let text = Array.from(document.querySelectorAll('#video-title'), el => el.innerHTML)
		return text
	})
	console.log(arr)
	browser.close()
})()


/*
const agent = new https.Agent({
  rejectUnauthorized: false
});
const fetchTitles = async () => {
	try {
	 const response = await axios.get(notariatru, { httpsAgent: agent });
   
		   const html = response.data;
   
	 const $ = cheerio.load(html);
   
	 const titles = [];
   
	 $('div.w-100 > h5').each((_idx, el) => {
	  const title = $(el).text()
	  titles.push(title)
	 });
   
	 return titles;
	} catch (error) {
	 throw error;
	}
   };
   
   fetchTitles().then((titles) => console.log(titles));
*/
