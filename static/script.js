$(document).ready(function () {
    // Load companies into dropdown list on page load please note the companies are comming from database
    $.get("/get_companies", function (data, status) {
        if (status === "success") {
            let companies = data["companies"];
            let dropdown = $("#companies");
            $.each(companies, function (index, company) {
                dropdown.append($("<option></option>").attr("value", company).text(company));
            });
        }
    });

    $("#analyzeButton").click(function () {
        let selectedCompany = $("#companies").val();
        if (selectedCompany) {
            // Show loader
            $("#loader").show();

            $.ajax({
                type: "POST",
                url: "/analyse_competitors",
                contentType: "application/json",
                data: JSON.stringify({ "name": selectedCompany }),
                
                // success: function (response) {
                    
                //     $("#loader").hide();

                //     $("#response").text(response.message);
                // },

                success: function (response) {
                    $("#loader").hide();
                
                    // Split the response by numbering
                    let competitors = response.message.split(/\d+\.\s*/);
                    competitors.shift(); // Remove empty first element
                
                    // Create an HTML table with numbering
                    let table = "<table>";
                    for (let i = 0; i < competitors.length; i++) {
                        table += "<tr><td>" + (i + 1) + ".</td><td>" + competitors[i] + "</td></tr>";
                    }
                    table += "</table>";
                
                    // Display the table in the response div
                    $("#response").html(table);
                },                
                
                error: function () {
                    
                    $("#loader").hide();

                    $("#response").text("An error occurred.");
                }
            });
        }
    });

});
