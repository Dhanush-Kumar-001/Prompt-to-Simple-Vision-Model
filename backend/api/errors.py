from fastapi import HTTPException, status


class InvalidPromptError(HTTPException):
    def __init__(self, detail="Invalid or empty prompt"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )


class PipelineBuildError(HTTPException):
    def __init__(self, detail="Failed to build pipeline"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail
        )


class UnsupportedTaskError(HTTPException):
    def __init__(self, detail="Unsupported task requested"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )
