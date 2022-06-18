// version 0.0.2
;(function ($, win, doc) { 'use strict';
    $.fn.jcolumn = function (options) { 
                
    var elements = this,
    
    defaults = {
        delay: 500,
        maxWidth: 767,
        callback: null
    }, 
    
    settings = $.extend( {}, defaults, options),
    
    // otherwise the event would trigger the function to fast
    delay = (function () {
		var timer = 0;
	  	return function(callback, ms){
	    	clearTimeout(timer);
	    	timer = setTimeout(callback, ms);
	  	};
	})(), 

	resizeColumn = function (rows) { 
		var elemH = 0;
            
		if ($(doc).width() >= settings.maxWidth) {
            rows.each(function () {
			    var $this = $(this);
			    $this.height('auto');
                
			    if ($this.height() > elemH) {
				    elemH = $this.height();
			    }
		    });
            
			rows.each(function () {
				$(this).height(elemH);
			});
            
            settings.callback(elemH);
		}
	};
    
	win.addEventListener('resize', function() {
		delay(resizeColumn(elements), settings.delay);
	});
    
    resizeColumn(elements); // init
    return this;
};}(jQuery, window, document));