function file1(h,i,j,k,l){
  $('#TotalCases').prop('Counter',0).animate({

        Counter: h
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
      
      $('#ActiveCases').prop('Counter',0).animate({

        Counter: i
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
      $('#DeathCases').prop('Counter',0).animate({
        Counter: j
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
      $('#RecoverdCases').prop('Counter',0).animate({
        Counter: k
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
       $('#MigratedCases').prop('Counter',0).animate({
        Counter: l
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });

      
      }
