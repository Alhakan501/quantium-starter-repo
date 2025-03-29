#!/bin/bash
set -euo pipefail
set e




check_git_changes() {
    echo "Checking Git status..."
    if [[ -n $(git status --porcelain) ]]; then
        echo -e "\nCommitting changes..."
        sleep 1
        git add .
        if git commit -m "$1"; then
                echo -e "\nCommit successful!"
        else
            echo -e "\n❌ Commit operation failed"
            exit 0
        fi
    else
        echo "✅ Clean working directory"
    fi
}





git_push(){
    check_git_changes $1
    sleep 1
    echo -e "\nPushing changes to GitHub..."
    sleep 1
   git remote set-url origin https://github.com/Alhakan501/quantium-starter-repo.git

    if git push origin main; then
        echo -e "\n✅ Successfully pushed to GitHub"
        exit 0
    else
        echo -e "\n❌ Push failed with error code $?"
        exit 1 
    fi

}











echo "----- Checking for test files -----"
sleep 1
echo " 🧪 Running integration tests from: "
sleep 2
if pytest -v app_tests/; then
        echo ""
        echo "✅ All integration tests passed!"
        echo ""
        
while true; do
        read -rp "Would you like to push your changes? (yes/no): " answer
        case $answer in [Yy]|[Yy][Ee][Ss])
            read -rp "Enter commit message: " message
                if [ -z "$message" ]; then
                    echo "❌ Commit message cannot be empty"
                    continue
                fi
            git_push "$message"
            exit 0
            ;;
        [Nn]|[Nn][Oo])
            echo "Changes not pushed"
                exit 0
                ;;
                *)
            echo "Please answer yes or no"
                ;;
            esac
        done
    else
        echo ""
        echo "❌ Integration tests failed!"
        echo "Fix the issues before pushing changes"
        exit 1
    fi

