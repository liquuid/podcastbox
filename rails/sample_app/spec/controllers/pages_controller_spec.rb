require 'spec_helper'
describe 'LayoutLinks' do
    render_views


    it "should have the right links on the layout" do
        visit root_path
        click_link "About"
        response.should have_selector('title', :content => 'about')
        click_link "Help"
        response.should have_selector('title', :content => 'help')
        click_link "Contact"
        response.should have_selector('title', :content => 'contact')
        click_link "Home"
        response.should have_selector('title', :content => 'home')
        click_link "Sign up now!"
        response.should have_selector('title', :content => 'sign up!')
    end
end
        
describe PagesController do
    render_views

    describe "GET 'home'" do
        it "should be successful" do
            get 'home'
            response.should be_success
        end

        it "should have the right title" do
            get "home"
            response.should have_selector("title", :content => "Ruby on Rails | home")
        end
    end

    describe "GET 'contact'" do
        it "should be successful" do
            get 'contact'
            response.should be_success
        end

        it "should have the right title" do
            get "contact"
            response.should have_selector("title", :content => "Ruby on Rails | contact")
        end
    end

    describe "GET 'about'" do
        it "should be successful" do
            get 'about'
            response.should be_success
        end

        it "should have the right title" do
            get "about"
            response.should have_selector("title", :content => "Ruby on Rails | about")
        end
    end
end
