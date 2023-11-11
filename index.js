const  punycode  =  require ( 'punycode/' ) ;
const axios = require("axios");
const cheerio = require("cheerio");
const https = require('https');

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

//let notariatru = punycode.toASCII('агеева');
let notariatru = 'https://' + punycode.toASCII('нотариус-агеева.рф');
//https://xn----7sb${notariatru}.xn--p1ai/

//const agent = new https.Agent({ ca: MY_CA_BUNDLE });


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
/*
notariat.ru
let i = encodeURIComponent('агеева')
console.log(`https://xn----7sb${i}.xn--p1ai/`)

//https://xn----7sbbajfoaw2clzoks.xn--p1ai/

*/
/*
//npm cache clean --forcenpm cache verify
npm uninstall yourPackage
npm uninstall -g yourPackage
//npm run start
*/