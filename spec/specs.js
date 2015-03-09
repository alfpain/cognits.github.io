describe("Cognits landing page", function(){

  it("should have link with logo on top", function(){
    expect($(".navbar-brand").text()).toBe("Cognits");
  });

});
