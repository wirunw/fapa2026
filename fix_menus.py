"""
Script to properly update navigation menus across all HTML files
This version carefully replaces only the menu content without breaking HTML structure
"""

import os
import re

# Page-specific active states
PAGES_ACTIVE = {
    'index.html': ('Home', 'gray-700'),
    'welcome.html': ('About', 'welcome'),
    'about.html': ('About', 'about'),
    'committee.html': ('About', 'committee'),
    'theme.html': ('Program', 'theme'),
    'schedule.html': ('Program', 'schedule'),
    'keynote.html': ('Program', 'keynote'),
    'invited.html': ('Program', 'invited'),
    'program.html': ('Program', 'program'),
    'abstracts.html': ('Abstracts', None),
    'register.html': ('Register', None),
    'venue.html': ('Venue', 'venue'),
    'accommodation.html': ('Venue', 'accommodation'),
    'thailand.html': ('Venue', 'thailand'),
    'sponsors.html': ('Sponsors', 'sponsors'),
    'socialevents.html': ('Sponsors', 'socialevents'),
    'tours.html': ('Sponsors', 'tours'),
    'news.html': ('Info', 'news'),
    'faq.html': ('Info', 'faq'),
    'students.html': ('Info', 'students'),
    'contact.html': ('Info', 'contact'),
}


def get_desktop_menu(active_section, active_page):
    """Generate desktop menu HTML with proper active states"""
    
    # Determine active classes
    home_class = 'blue-600' if active_section == 'Home' else 'gray-700'
    about_class = 'blue-600 hover:text-blue-700' if active_section == 'About' else 'gray-700 hover:text-blue-600'
    program_class = 'blue-600 hover:text-blue-700' if active_section == 'Program' else 'gray-700 hover:text-blue-600'
    abstracts_class = 'blue-600' if active_section == 'Abstracts' else 'gray-700'
    register_class = 'blue-600' if active_section == 'Register' else 'gray-700'
    venue_class = 'blue-600 hover:text-blue-700' if active_section == 'Venue' else 'gray-700 hover:text-blue-600'
    sponsors_class = 'blue-600 hover:text-blue-700' if active_section == 'Sponsors' else 'gray-700 hover:text-blue-600'
    info_class = 'blue-600 hover:text-blue-700' if active_section == 'Info' else 'gray-700 hover:text-blue-600'
    
    # Determine submenu highlights
    def get_submenu_class(page_key):
        return ' bg-blue-50' if active_page == page_key else ''
    
    return f'''                <!-- Desktop Menu -->
                <div class="hidden md:flex items-center space-x-6">
                    <a href="index.html" class="text-{home_class} hover:text-blue-600 font-medium transition">Home</a>
                    <div class="relative dropdown">
                        <button class="text-{about_class} font-medium flex items-center cursor-pointer">
                            About
                            <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-56 bg-white shadow-xl rounded-lg py-2 mt-0">
                            <a href="welcome.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('welcome')}">Welcome Messages</a>
                            <a href="about.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('about')}">About FAPA & PAT</a>
                            <a href="committee.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('committee')}">Organizing Committee</a>
                        </div>
                    </div>
                    <div class="relative dropdown">
                        <button class="text-{program_class} font-medium flex items-center cursor-pointer">
                            Program
                            <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-56 bg-white shadow-xl rounded-lg py-2 mt-0">
                            <a href="theme.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('theme')}">Theme & Topics</a>
                            <a href="schedule.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('schedule')}">Program at a Glance</a>
                            <a href="keynote.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('keynote')}">Keynote Speakers</a>
                            <a href="invited.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('invited')}">Invited Speakers</a>
                            <a href="program.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('program')}">Detailed Program</a>
                        </div>
                    </div>
                    <a href="abstracts.html" class="text-{abstracts_class} hover:text-blue-600 font-medium transition">Abstracts</a>
                    <a href="register.html" class="text-{register_class} hover:text-blue-600 font-medium transition">Register</a>
                    <div class="relative dropdown">
                        <button class="text-{venue_class} font-medium flex items-center cursor-pointer">
                            Venue
                            <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-56 bg-white shadow-xl rounded-lg py-2 mt-0">
                            <a href="venue.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('venue')}">Conference Venue</a>
                            <a href="accommodation.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('accommodation')}">Accommodation</a>
                            <a href="thailand.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('thailand')}">About Thailand</a>
                        </div>
                    </div>
                    <div class="relative dropdown">
                        <button class="text-{sponsors_class} font-medium flex items-center cursor-pointer">
                            Sponsors
                            <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-56 bg-white shadow-xl rounded-lg py-2 mt-0">
                            <a href="sponsors.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('sponsors')}">Sponsorship & Exhibition</a>
                            <a href="socialevents.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('socialevents')}">Social Events</a>
                            <a href="tours.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('tours')}">Tours</a>
                        </div>
                    </div>
                    <div class="relative dropdown">
                        <button class="text-{info_class} font-medium flex items-center cursor-pointer">
                            Info
                            <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-56 bg-white shadow-xl rounded-lg py-2 mt-0">
                            <a href="news.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('news')}">News & Updates</a>
                            <a href="faq.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('faq')}">FAQ</a>
                            <a href="students.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('students')}">Student Assistants</a>
                            <a href="contact.html" class="block px-4 py-2 text-gray-700 hover:bg-blue-50{get_submenu_class('contact')}">Contact Us</a>
                        </div>
                    </div>
                </div>'''


def get_mobile_menu(active_section, active_page):
    """Generate mobile menu HTML with proper active states"""
    
    def get_mobile_class(section, page_key=None):
        if section == active_section:
            if page_key:
                return 'blue-600 font-medium' if active_page == page_key else 'gray-700 hover:text-blue-600'
            return 'blue-600 font-medium'
        return 'gray-700 hover:text-blue-600'
    
    return f'''        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t">
            <div class="px-4 pt-2 pb-4 space-y-2">
                <a href="index.html" class="block py-2 text-{get_mobile_class('Home')}">Home</a>
                
                <div class="border-t pt-2 mt-2">
                    <p class="text-xs font-semibold text-gray-500 uppercase mb-1">About</p>
                    <a href="welcome.html" class="block py-2 pl-4 text-{get_mobile_class('About', 'welcome')}">Welcome Messages</a>
                    <a href="about.html" class="block py-2 pl-4 text-{get_mobile_class('About', 'about')}">About FAPA & PAT</a>
                    <a href="committee.html" class="block py-2 pl-4 text-{get_mobile_class('About', 'committee')}">Organizing Committee</a>
                </div>
                
                <div class="border-t pt-2 mt-2">
                    <p class="text-xs font-semibold text-gray-500 uppercase mb-1">Program</p>
                    <a href="theme.html" class="block py-2 pl-4 text-{get_mobile_class('Program', 'theme')}">Theme & Topics</a>
                    <a href="schedule.html" class="block py-2 pl-4 text-{get_mobile_class('Program', 'schedule')}">Program at a Glance</a>
                    <a href="keynote.html" class="block py-2 pl-4 text-{get_mobile_class('Program', 'keynote')}">Keynote Speakers</a>
                    <a href="invited.html" class="block py-2 pl-4 text-{get_mobile_class('Program', 'invited')}">Invited Speakers</a>
                    <a href="program.html" class="block py-2 pl-4 text-{get_mobile_class('Program', 'program')}">Detailed Program</a>
                </div>
                
                <a href="abstracts.html" class="block py-2 text-{get_mobile_class('Abstracts')} border-t pt-2 mt-2">Abstracts</a>
                <a href="register.html" class="block py-2 text-{get_mobile_class('Register')}">Register</a>
                
                <div class="border-t pt-2 mt-2">
                    <p class="text-xs font-semibold text-gray-500 uppercase mb-1">Venue & Travel</p>
                    <a href="venue.html" class="block py-2 pl-4 text-{get_mobile_class('Venue', 'venue')}">Conference Venue</a>
                    <a href="accommodation.html" class="block py-2 pl-4 text-{get_mobile_class('Venue', 'accommodation')}">Accommodation</a>
                    <a href="thailand.html" class="block py-2 pl-4 text-{get_mobile_class('Venue', 'thailand')}">About Thailand</a>
                </div>
                
                <div class="border-t pt-2 mt-2">
                    <p class="text-xs font-semibold text-gray-500 uppercase mb-1">Sponsors & Events</p>
                    <a href="sponsors.html" class="block py-2 pl-4 text-{get_mobile_class('Sponsors', 'sponsors')}">Sponsorship & Exhibition</a>
                    <a href="socialevents.html" class="block py-2 pl-4 text-{get_mobile_class('Sponsors', 'socialevents')}">Social Events</a>
                    <a href="tours.html" class="block py-2 pl-4 text-{get_mobile_class('Sponsors', 'tours')}">Tours</a>
                </div>
                
                <div class="border-t pt-2 mt-2">
                    <p class="text-xs font-semibold text-gray-500 uppercase mb-1">Information</p>
                    <a href="news.html" class="block py-2 pl-4 text-{get_mobile_class('Info', 'news')}">News & Updates</a>
                    <a href="faq.html" class="block py-2 pl-4 text-{get_mobile_class('Info', 'faq')}">FAQ</a>
                    <a href="students.html" class="block py-2 pl-4 text-{get_mobile_class('Info', 'students')}">Student Assistants</a>
                    <a href="contact.html" class="block py-2 pl-4 text-{get_mobile_class('Info', 'contact')}">Contact Us</a>
                </div>
            </div>
        </div>'''


def update_file(filename):
    """Update navigation menus in a single HTML file"""
    if filename not in PAGES_ACTIVE:
        print(f"⊘ Skipping {filename} - not in pages list")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        active_section, active_page = PAGES_ACTIVE[filename]
        
        # Generate new menus
        new_desktop = get_desktop_menu(active_section, active_page)
        new_mobile = get_mobile_menu(active_section, active_page)
        
        # Replace desktop menu - find between logo div and mobile button
        desktop_pattern = r'(</a>\s*</div>\s*)<!-- Desktop Menu -->.*?</div>(\s*<!-- Mobile menu button -->)'
        if not re.search(desktop_pattern, content, re.DOTALL):
            print(f"✗ {filename}: Could not find desktop menu pattern")
            return False
        content = re.sub(desktop_pattern, r'\1' + new_desktop + r'\n\n\2', content, flags=re.DOTALL)
        
        # Replace mobile menu
        mobile_pattern = r'<!-- Mobile Menu -->.*?</div>\s*</div>\s*</nav>'
        if not re.search(mobile_pattern, content, re.DOTALL):
            print(f"✗ {filename}: Could not find mobile menu pattern")
            return False
        content = re.sub(mobile_pattern, new_mobile + '\n    </nav>', content, flags=re.DOTALL)
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename}")
        return True
        
    except Exception as e:
        print(f"✗ {filename}: {str(e)}")
        return False


def main():
    """Update all HTML files"""
    files = sorted([f for f in os.listdir('.') if f.endswith('.html') and f in PAGES_ACTIVE])
    
    print(f"Updating {len(files)} HTML files...\n")
    
    success = 0
    for filename in files:
        if update_file(filename):
            success += 1
    
    print(f"\n{'='*60}")
    print(f"Successfully updated {success}/{len(files)} files")
    
    if success < len(files):
        print("\nSome files failed. Check the output above for details.")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
