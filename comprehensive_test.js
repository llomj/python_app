// COMPREHENSIVE SOLUTION TAB TEST FOR GITHUB PAGES
// Run this in browser console at: https://llomj.github.io/python_app/

console.log('🚀 COMPREHENSIVE SOLUTION TAB TEST');
console.log('=====================================');

// Test 1: Check if solution button exists
function findSolutionButton() {
    // Try multiple selectors for the solution button
    const selectors = [
        'button[description="Sol"]',
        'button:has([title*="Sol"])',
        'button[title*="Sol"]',
        'button[data-sol]',
        'button.sol-btn'
    ];

    for (const selector of selectors) {
        const btn = document.querySelector(selector);
        if (btn) {
            console.log('✅ Solution button found with selector:', selector);
            return btn;
        }
    }

    // Try finding by text content
    const buttons = Array.from(document.querySelectorAll('button'));
    const solBtn = buttons.find(btn =>
        btn.textContent.includes('Sol') ||
        btn.getAttribute('description') === 'Sol' ||
        btn.getAttribute('title')?.includes('Sol')
    );

    if (solBtn) {
        console.log('✅ Solution button found by text/content');
        return solBtn;
    }

    console.log('❌ Solution button NOT found');
    console.log('Available buttons:', buttons.map(btn =>
        `${btn.textContent || 'no-text'} (${btn.getAttribute('description') || 'no-desc'})`
    ).filter(Boolean));
    return null;
}

// Test 2: Test fetch functionality
async function testFetchRequests() {
    console.log('🌐 Testing fetch requests...');

    const tests = [
        { url: '/level1_500_codelogic.py', name: 'Logic file' },
        { url: '/level1_500_requirements.py', name: 'Requirements file' },
        { url: '/level1_1000_codelogic.py', name: 'Level 1000 Logic' },
        { url: '/level1_2000_requirements.py', name: 'Level 2000 Requirements' }
    ];

    for (const test of tests) {
        try {
            const response = await fetch(test.url);
            const status = response.status;
            const ok = response.ok;

            if (ok) {
                const text = await response.text();
                console.log(`✅ ${test.name}: ${status} OK - ${text.length} chars`);
            } else {
                console.log(`❌ ${test.name}: ${status} FAILED`);
            }
        } catch (error) {
            console.log(`❌ ${test.name}: ERROR - ${error.message}`);
        }
    }
}

// Test 3: Test extractProblemContent function
function testExtractFunction() {
    console.log('🔍 Testing extractProblemContent function...');

    // Test with sample content
    const sampleContent = `"""
Problem 40:
Write a Python function called find_min_max...

def find_min_max(numbers):
    min_number = numbers[0]
    max_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
    return min_number, max_number

"""
Problem 41:
Next problem...
"""`;

    const extracted = extractProblemContent(sampleContent, 40);
    console.log('🔍 Extract test result length:', extracted.length);
    console.log('🔍 Extract test preview:', extracted.substring(0, 100) + '...');

    if (extracted.length > 50) {
        console.log('✅ Extract function works correctly');
    } else {
        console.log('❌ Extract function FAILED');
    }
}

// Test 4: Simulate clicking solution tabs
async function testSolutionTabs() {
    console.log('🎯 Testing solution tab clicks...');

    // Find solution button
    const solBtn = findSolutionButton();
    if (!solBtn) return;

    // Click solution button
    console.log('🔧 Clicking solution button...');
    solBtn.click();

    // Wait for modal to appear
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Find Logic and Requirements tabs
    const logicBtn = Array.from(document.querySelectorAll('button')).find(btn =>
        btn.textContent.trim().toLowerCase() === 'logic'
    );

    const reqBtn = Array.from(document.querySelectorAll('button')).find(btn =>
        btn.textContent.trim().toLowerCase() === 'requirements'
    );

    console.log('🔍 Logic tab found:', !!logicBtn);
    console.log('🔍 Requirements tab found:', !!reqBtn);

    if (logicBtn) {
        console.log('✅ Testing Logic tab click...');
        logicBtn.click();

        // Check for content after 2 seconds
        setTimeout(() => {
            const contentDiv = document.querySelector('[data-problem-description]');
            if (!contentDiv) {
                console.log('❌ No content div found');
                return;
            }

            const content = contentDiv.textContent || '';
            if (content.length > 10) {
                console.log('✅ Logic tab SUCCESS - Content found:', content.length, 'chars');
                console.log('📄 Preview:', content.substring(0, 100) + '...');
            } else {
                console.log('❌ Logic tab FAILED - No content loaded');
                console.log('Current content:', content);
            }
        }, 2000);
    }

    if (reqBtn) {
        console.log('✅ Testing Requirements tab click...');
        reqBtn.click();

        // Check for content after 2 seconds
        setTimeout(() => {
            const contentDiv = document.querySelector('[data-problem-description]');
            if (!contentDiv) {
                console.log('❌ No content div found for requirements');
                return;
            }

            const content = contentDiv.textContent || '';
            if (content.length > 10) {
                console.log('✅ Requirements tab SUCCESS - Content found:', content.length, 'chars');
                console.log('📄 Preview:', content.substring(0, 100) + '...');
            } else {
                console.log('❌ Requirements tab FAILED - No content loaded');
                console.log('Current content:', content);
            }
        }, 2500);
    }
}

// Test 5: Check service worker
function checkServiceWorker() {
    console.log('🔧 Checking service worker...');

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.getRegistrations().then(registrations => {
            console.log('📋 SW Registrations:', registrations.length);

            registrations.forEach(registration => {
                console.log('📍 SW Scope:', registration.scope);
                console.log('🔄 Active:', !!registration.active);
                console.log('📱 Installing:', !!registration.installing);
                console.log('⏳ Waiting:', !!registration.waiting);
            });
        });
    } else {
        console.log('❌ No service worker support');
    }
}

// Extract problem content function (same as in app)
function extractProblemContent(fileContent, problemId) {
    const problemMarker = new RegExp(`"""\\s*Problem\\s*:?\\s*${problemId}\\b`, 'm');
    const match = fileContent.match(problemMarker);

    if (!match) {
        return '';
    }

    const startIndex = match.index || 0;
    const remainingContent = fileContent.substring(startIndex);
    const nextProblemPattern = new RegExp(`"""\\s*Problem\\s*:?\\s*\\d+\\b`, 'm');

    let endIndex = remainingContent.length;
    let searchStart = match[0].length;

    while (searchStart < remainingContent.length) {
        const nextMatch = remainingContent.substring(searchStart).match(nextProblemPattern);
        if (!nextMatch) {
            break;
        }

        const nextProblemNum = nextMatch[0].match(/\d+/);
        if (nextProblemNum && parseInt(nextProblemNum[0]) !== problemId) {
            endIndex = searchStart + (nextMatch.index || 0);
            break;
        }

        searchStart += (nextMatch.index || 0) + nextMatch[0].length;
    }

    return remainingContent.substring(0, endIndex).trim();
}

// RUN ALL TESTS
async function runAllTests() {
    console.log('🚀 STARTING COMPREHENSIVE TESTS');
    console.log('=====================================');

    checkServiceWorker();
    await testFetchRequests();
    testExtractFunction();
    await testSolutionTabs();

    console.log('=====================================');
    console.log('✅ ALL TESTS COMPLETED');
    console.log('Check results above for SUCCESS/FAILURE');
}

// Execute tests after page load
if (document.readyState === 'loading') {
    window.addEventListener('load', () => setTimeout(runAllTests, 2000));
} else {
    setTimeout(runAllTests, 2000);
}

console.log('⏳ Tests will run automatically in 2 seconds...');