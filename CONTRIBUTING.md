# How to Contribute Code to EnergyVision

Thank you for your interest in contributing to EnergyVision! We strongly welcome and appreciate your contributions. This guide is intended to make the process as quick and painless as possible.

> **Note:**  
> These guidelines are intended for most contributions. They are not "one-size-fits-all" rules—if you are unsure how to structure your contribution, please reach out. We’re always happy to help and provide feedback.

## Your Code Contribution

The source code for EnergyVision is hosted on [GitHub](https://github.com/consandrade/EnergyVision). All changes are submitted via pull requests (PRs), and the primary branch for development is `main`.

> **Important:**  
> We require that PRs apply cleanly to `main` without merge commits (i.e., via fast-forward merges). Please adhere to our coding conventions as detailed in our [Style Guide](STYLE_GUIDE.md). Following these conventions helps reviewers and keeps our project consistent. For your convenience, configuration files (such as for code formatters) are provided in the repository.

By contributing code, you agree to transfer your copyright on the contributed code to the EnergyVision project. Rest assured, you will be duly credited.

## Your Commit

Each commit should represent a self-contained, atomic change. This means:

1. **Each commit must build EnergyVision successfully.**  
   This makes it easier to traverse the git history (e.g., with `git bisect`) and ensures that the project remains in a functional state at all times.
2. **Each commit should focus on one independent change.**  
   This enables us to revert a change if necessary without affecting unrelated parts of the project.

> **Tip:**  
> During development, it can be useful to create smaller commits to track intermediate changes. However, before submitting a pull request, please rebase or squash your commits to ensure they adhere to these guidelines and to keep the commit history clean.

### Your Commit Message

The commit summary (the first line of the commit message) should be preceded by a scope tag—enclosed in square brackets—that indicates which part of EnergyVision is affected (e.g., `[data]`, `[UI]`, `[processing]`). If you’re unsure which tag to use, please ask or check our commit history for examples.

The summary should be concise (maximum 50 characters, excluding the scope tag), meaningful, and written in the [present imperative mood](https://git.kernel.org/pub/scm/git/git.git/tree/Documentation/SubmittingPatches?id=HEAD#n239) (for example, `Add new feature` rather than `Added new feature`).

If additional context is needed, include a commit body that explains the **why** behind your change (the diff already shows the **what** and **how**). Wrap this text at 72 characters.

> **Tip:**  
> We provide a commit message template in the repository as [`.git-commit-template`](.git-commit-template). To automatically use it for every commit, run:
> ```sh
> git config commit.template .git-commit-template
> ```

## Your Pull Request

> **Note:**  
> For detailed instructions on creating pull requests, please refer to our [Pull Request Guide](https://github.com/yourusername/EnergyVision/blob/main/CONTRIBUTING.md).

Your pull request title should follow the same principles as your commit summary. If your PR contains only a single commit, you may reuse the summary. For non-functional changes (e.g., documentation updates) or for draft PRs (to temporarily disable automated checks), you may prepend `[skip-CI]` to your title. For functional changes, ensure that any such tags are removed so that the PR passes all CI checks before merging.

The PR description should provide a more detailed explanation of your change, particularly focusing on the **why** rather than just the **what** or **how**. If your PR relates to an open [issue](https://github.com/yourusername/EnergyVision/issues), please reference it (e.g., `Fixes #123`) so that it is automatically linked.

Once your PR is submitted, a member of the EnergyVision team will review your changes and provide feedback. If you do not receive timely feedback, feel free to politely ping the team.

## Tests

If your contribution fixes an issue or introduces a new feature, please include or update tests accordingly. Tests should be added in the relevant `test/` directories. This ensures that your changes are verified and that future modifications do not break existing functionality.

## Continuous Integration

EnergyVision uses automated Continuous Integration (CI) to ensure that all changes are stable and adhere to our quality standards:
- **Build and Test:** PRs are automatically built and tested. Please make sure your PR passes all tests before requesting a review.
- **Formatting Check:** Automated tools verify that your code follows our coding conventions as detailed in our [Style Guide](STYLE_GUIDE.md). If formatting issues are detected, instructions will be provided for correction.
- **Static Analysis:** Linters and static analysis tools run on your PR to catch potential issues early.

Thank you for taking the time to contribute to EnergyVision! Your efforts are essential to the project’s success, and we deeply appreciate your dedication.
