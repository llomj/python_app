// IMMEDIATE SOLUTION TAB TEST - Copy to browser console
console.log('🚀 IMMEDIATE SOLUTION TAB TEST');

// Check if React app is loaded
const reactRoot = document.getElementById('root');
console.log('React root found:', !!reactRoot);

// Check for solution button
setTimeout(() => {
    const buttons = Array.from(document.querySelectorAll('button'));
    const solBtn = buttons.find(btn =>
        btn.textContent.includes('Sol') ||
        btn.getAttribute('description') === 'Sol'
    );

    console.log('Solution button found:', !!solBtn);
    if (solBtn) {
        console.log('Button text:', solBtn.textContent);
        console.log('Button attributes:', solBtn.getAttribute('description'));

        // Try clicking it
        console.log('Clicking solution button...');
        solBtn.click();

        // Check for modal after click
        setTimeout(() => {
            const modal = document.querySelector('[class*="modal"], [class*="solution"]');
            console.log('Modal found after click:', !!modal);

            // Check for Logic/Requirements tabs
            const logicTab = Array.from(document.querySelectorAll('button')).find(btn =>
                btn.textContent.trim().toLowerCase() === 'logic'
            );

            const reqTab = Array.from(document.querySelectorAll('button')).find(btn =>
                btn.textContent.trim().toLowerCase() === 'requirements'
            );

            console.log('Logic tab found:', !!logicTab);
            console.log('Requirements tab found:', !!reqTab);

            if (logicTab) {
                console.log('Clicking Logic tab...');
                logicTab.click();

                setTimeout(() => {
                    // Check if any content loaded
                    const codeMirror = document.querySelector('[class*="CodeMirror"], [class*="codemirror"]');
                    const contentDiv = document.querySelector('[data-problem-description]');
                    const loadingText = document.querySelector('div')?.textContent?.includes('Searching');

                    console.log('CodeMirror found:', !!codeMirror);
                    console.log('Content div found:', !!contentDiv);
                    console.log('Loading text found:', !!loadingText);

                    if (contentDiv) {
                        console.log('Content div text:', contentDiv.textContent?.substring(0, 100));
                    }

                    console.log('✅ LOGIC TAB TEST COMPLETE');
                }, 2000);
            }
        }, 1000);
    } else {
        console.log('❌ Solution button NOT found');
        console.log('All buttons:', buttons.map(btn =>
            `${btn.textContent || 'no-text'} (${btn.getAttribute('description') || 'no-desc'})`
        ));
    }
}, 3000);