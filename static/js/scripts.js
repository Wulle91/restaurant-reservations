var occupied_dates = [];
        var occupied_tables = [];
        {% for date in dates %}
            var date = "{{date.reservation_date}}"
            var table = "{{date.table}}"
            occupied_dates.push(date.slice(0,-10))
            occupied_tables.push(table)
        {% endfor %}
        
        var emails = []
        console.log(emails)
        {% for reservation in reservations %}
            var email = "{{reservation.email}}"
            emails.push(email)   
        {% endfor %}

        let liElements = document.getElementsByClassName('your_booked-dates');
        var indexes = getAllIndexes(emails, "{{user.email}}");
        var tables = document.getElementsByClassName('Table');
 
        function getAllIndexes(arr, val) {
            var indexes = [], i = -1;
            while ((i = arr.indexOf(val, i+1)) != -1){
                indexes.push(i);
                }
            return indexes;
        }

        for (let i=0; i<indexes.length; i++){
            liElements[indexes[i]].removeAttribute('hidden')
        }

        var date = document.getElementById('date')
        date.addEventListener("change",() =>{
            addOnclick();
            searchDates();    
        });

        function addOnclick() {
            for (let i = 1; i <= 5; i++) {
                document.getElementById("Table" + i).onclick = inputDataWindow;
            }
        }
       
        function searchDates() {
            for (let i=0; i<occupied_dates.length; i++) {
                document.getElementById("Table"+occupied_tables[i]).style.backgroundColor='white'
                document.getElementById("Table"+occupied_tables[i]).setAttribute('onclick', 'inputDataWindow()');
            }
            let clickedDate = new Date(event.target.value); 
            formattedDate = clickedDate.toLocaleDateString("en-US", { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric', 
            });
            var dateCorected = formattedDate
            for (let i=0; i<occupied_dates.length; i++) {
                if(occupied_dates[i] == dateCorected) {
                    document.getElementById("Table"+occupied_tables[i]).style.backgroundColor='red';
                    document.getElementById("Table"+occupied_tables[i]).removeAttribute('onclick');
                }
            }
        }

        function inputDataWindow(){
            let reservation_container = document.getElementById("reservation")
                reservation_container.removeAttribute("hidden")
            }
        
        
        function edit(date_id){  
            let edit_reservation = document.getElementById("edit_reservation")
            let edit_form = document.getElementById("edit_form")
            let reservation_id = parseInt(date_id) + 165
            edit_reservation.removeAttribute("hidden")
            document.getElementById("new_comment").setAttribute("placeholder", reservation_id);
            document.getElementById("new_phone").setAttribute("placeholder", reservation_id);
            edit_form.setAttribute("action", "/edit/" + date_id)
            let comment_id = document.getElementById("new_comment").getAttribute("placeholder");
            
            {% for reservation in reservations %}
                if ({{reservation.id}} == comment_id) {
                    document.getElementById("new_phone").placeholder = `{{reservation.phone_number}}`;
                    document.getElementById("new_comment").placeholder = `{{reservation.comment}}`;
                }
            {% endfor %}
        } 

        function close_edit_container() {
            document.getElementById("edit_reservation").setAttribute('hidden', 'true');
        }

        function confirm_comment_delete(x) {
            document.getElementById("delete_comment" + x).removeAttribute('hidden');
            document.getElementById("delete_comment_button" + x).setAttribute('hidden', 'true');
        }

        function close_delete_comment(x) {
            document.getElementById("delete_comment" + x).setAttribute('hidden', 'true');
            document.getElementById("delete_comment_button" + x).removeAttribute('hidden');
        }

        function open_delete_window(x) {
            document.getElementById("delete_date" + x).removeAttribute('hidden');
            document.getElementById("delete_comment_btn" + x).setAttribute('hidden', 'true');
            document.getElementById("edit" + x).setAttribute('hidden', 'true');
        }

        function close_delete_window(x) {
            document.getElementById("delete_date" + x).setAttribute('hidden', 'true');
            document.getElementById("delete_comment_btn" + x).removeAttribute('hidden');
            document.getElementById("edit" + x).removeAttribute('hidden');
        }

        function close_reservation_window() {
            document.getElementById("reservation").setAttribute('hidden', 'true');
        }