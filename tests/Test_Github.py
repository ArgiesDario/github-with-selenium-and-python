import pytest
from misc.config_data import *
from misc.BrowserSetup import BrowserSetup
from pages.github_searchpage import GithubSearchPage
from pages.github_advanced_searchpage import GithubAdvancedSearchPage
from pages.github_repopage import GithubRepoPage


class Test_Github:

    def set_up(self, url):
        self.browser = BrowserSetup()
        self.search_page = GithubSearchPage(self.browser.get_driver())
        self.advanced_search_page = GithubAdvancedSearchPage(self.browser.get_driver())
        self.repo_page = GithubRepoPage(self.browser.get_driver())
        self.browser.get_driver().get(url)

    def tear_down(self):
        self.browser.close_driver()

    @pytest.mark.parametrize(
        "github_url,search_for,language,stars_amount,followers_amount,license,repository_name",
        [
            # TC 1 - Advance search in Github
            (github_url, "react", "JavaScript", ">45", ">50", "Boost Software License 1.0", 'mvoloskov/decider'),
        ]
    )
    def test_Login_Logout(self, github_url, search_for, language, stars_amount, followers_amount, license,
                          repository_name):
        self.set_up(github_url)

        # Search for React on the general page
        self.search_page.perform_search(search_for)
        self.search_page.advanced_search_link_click()

        # Perform an advance search
        self.advanced_search_page.written_language_select_option(language)
        self.advanced_search_page.stars_type(stars_amount)
        self.advanced_search_page.followers_type(followers_amount)
        self.advanced_search_page.license_select_option(license)
        self.advanced_search_page.search_button_click()

        # Validate there is only 1 result and repo name
        assert self.search_page.repository_found_get().strip() == '1 repository result'
        assert self.search_page.repository_name_get() == repository_name

        # Open repo and print 300 chars of readme
        self.search_page.repository_name_click()
        print(self.repo_page.readme_get()[:300])

        self.tear_down()
