$("#print_tab").click(function() {
	    var new_wnd = window.open(location.href+"?tmpl=component&print=1&layout=default&page=", "subWindow", "status,menubar,height=700,width=700,scrollbars=yes");
        var new_content = '<html><head><title>123</title><meta http-equiv="content-type" content="text/html; charset=utf-8" />'; 
		css_path = "<?php echo JURI::base().'css/style_print.css'; ?>"
		new_content += '<script type="text\/javascript">function ImportStyleFile () {'
        new_content +=    'var linkTag = document.createElement ("link");'
        new_content +=    'linkTag.href = "'+ css_path +'";'
        new_content +=    'linkTag.rel = "stylesheet";'
        new_content +=    'var head = document.getElementsByTagName ("head")[0];'
        new_content +=    'head.appendChild (linkTag);'
        new_content += '}<\/script>';
		new_content += '</head><body onload="ImportStyleFile()">';
		new_content += $("#main_tab").html();
		new_content += '</body><html>';
		new_wnd.document.write(new_content);
		new_wnd.document.close();
		new_wnd.print();
	  });