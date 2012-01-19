<!DOCTYPE html>
<html>
<head></head>
<body>
<!-- Piwik -->
<script type="text/javascript">
var pkBaseURL = (("https:" == document.location.protocol) ? "https://piwik.luxifer.fr/" : "http://piwik.luxifer.fr/");
document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));
</script><script type="text/javascript">
try {
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 1);
piwikTracker.trackPageView();
piwikTracker.enableLinkTracking();
} catch( err ) {}
</script><noscript><p><img src="http://piwik.luxifer.fr/piwik.php?idsite=1" style="border:0" alt="" /></p></noscript>
<!-- End Piwik Tracking Code -->
<script type="text/javascript">
var url = "{{ location }}";
var xhr; 
var shortened;
try {
  xhr = new ActiveXObject('Msxml2.XMLHTTP');
}
catch (e) {
  try {
    xhr = new ActiveXObject('Microsoft.XMLHTTP');
  }
  catch (e2) {
    try {
      xhr = new XMLHttpRequest();
    }
    catch (e3) {
      xhr = false;
    }
  }
}

xhr.onreadystatechange  = function() { 
  if(xhr.readyState  == 4) {
    if(xhr.status  == 200) {
      shortened = xhr.responseText; 
      window.open("https://twitter.com/share?url="+escape(shortened));
    }
    else {
      console.log('Error code ' + xhr.status);
    }
  }
};

 xhr.open('POST', 'http://{{ host }}/api/translate/raw', true);
 xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');  
 xhr.send('url='+escape(url));
</script>
</body>
</html>
